package vn.edu.ptit.campushub;

import static org.hamcrest.Matchers.greaterThanOrEqualTo;
import static org.springframework.security.test.web.servlet.request.SecurityMockMvcRequestPostProcessors.httpBasic;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.patch;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import com.jayway.jsonpath.JsonPath;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

@SpringBootTest
@AutoConfigureMockMvc
class PostApiIntegrationTest {
    @Autowired
    private MockMvc mockMvc;

    @Test
    void publicUserCanReadSeededPosts() throws Exception {
        mockMvc.perform(get("/api/posts"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.totalElements").value(greaterThanOrEqualTo(2)));
    }

    @Test
    void anonymousUserCannotCreatePost() throws Exception {
        mockMvc.perform(post("/api/posts")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {"title":"Bài mới","content":"Nội dung hợp lệ","categoryId":1}
                                """))
                .andExpect(status().isUnauthorized());
    }

    @Test
    void authenticatedUserCanCreatePost() throws Exception {
        mockMvc.perform(post("/api/posts")
                        .with(httpBasic("student", "student123"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {"title":"Tìm nhóm học DevOps","content":"Cần thêm hai thành viên cùng thực hành.","categoryId":6}
                                """))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.title").value("Tìm nhóm học DevOps"))
                .andExpect(jsonPath("$.author.username").value("student"));
    }

    @Test
    void invalidPostReturnsReadableMessage() throws Exception {
        mockMvc.perform(post("/api/posts")
                        .with(httpBasic("student", "student123"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {"title":"","content":"Nội dung","categoryId":1}
                                """))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.message").isNotEmpty());
    }

    @Test
    void userCanApplyForGroupMembershipAndAuthorCanApprove() throws Exception {
        String postResponse = mockMvc.perform(post("/api/posts")
                        .with(httpBasic("student", "student123"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {"title":"Tìm nhóm làm DevOps Session 13","content":"Cần 2 bạn làm cùng","categoryId":6,"targetMembers":2}
                                """))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.targetMembers").value(2))
                .andReturn().getResponse().getContentAsString();

        long postId = ((Number) JsonPath.read(postResponse, "$.id")).longValue();

        mockMvc.perform(post("/api/posts/" + postId + "/memberships")
                        .with(httpBasic("student", "student123"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {"message":"Em muốn tham gia","contactInfo":"0912345678"}
                                """))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.message").value("Bạn là chủ bài đăng, không thể tự ứng tuyển"));

        String applyResponse = mockMvc.perform(post("/api/posts/" + postId + "/memberships")
                        .with(httpBasic("admin", "admin123"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {"message":"Mình muốn tham gia nhóm DevOps","contactInfo":"admin@ptit.edu.vn"}
                                """))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.status").value("PENDING"))
                .andExpect(jsonPath("$.username").value("admin"))
                .andReturn().getResponse().getContentAsString();

        long membershipId = ((Number) JsonPath.read(applyResponse, "$.id")).longValue();

        mockMvc.perform(patch("/api/posts/" + postId + "/memberships/" + membershipId + "/status")
                        .with(httpBasic("student", "student123"))
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {"status":"ACCEPTED"}
                                """))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.status").value("ACCEPTED"));
    }
}
