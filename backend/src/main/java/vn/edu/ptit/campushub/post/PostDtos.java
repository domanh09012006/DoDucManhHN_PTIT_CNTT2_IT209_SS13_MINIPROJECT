package vn.edu.ptit.campushub.post;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import java.time.Instant;
import java.util.List;
import vn.edu.ptit.campushub.comment.Comment;
import vn.edu.ptit.campushub.membership.GroupMembership;
import vn.edu.ptit.campushub.membership.MembershipStatus;

public final class PostDtos {
    private PostDtos() {
    }

    public record PostRequest(
            @NotBlank(message = "Tiêu đề không được để trống")
            @Size(max = 160, message = "Tiêu đề tối đa 160 ký tự") String title,
            @NotBlank(message = "Nội dung không được để trống")
            @Size(max = 10000, message = "Nội dung tối đa 10.000 ký tự") String content,
            @NotNull(message = "Vui lòng chọn chuyên mục") Long categoryId,
            @Min(value = 1, message = "Số lượng thành viên tối thiểu là 1")
            @Max(value = 50, message = "Số lượng thành viên tối đa là 50") Integer targetMembers) {
    }

    public record StatusRequest(@NotNull(message = "Trạng thái không được để trống") PostStatus status) {
    }

    public record CommentRequest(
            @NotBlank(message = "Bình luận không được để trống")
            @Size(max = 1000, message = "Bình luận tối đa 1.000 ký tự") String content) {
    }

    public record ApplyMembershipRequest(
            @NotBlank(message = "Vui lòng nhập lời nhắn giới thiệu")
            @Size(max = 500, message = "Lời nhắn tối đa 500 ký tự") String message,
            @NotBlank(message = "Vui lòng nhập thông tin liên hệ (SĐT / Zalo / Facebook)")
            @Size(max = 100, message = "Thông tin liên hệ tối đa 100 ký tự") String contactInfo) {
    }

    public record MembershipStatusRequest(
            @NotNull(message = "Trạng thái không được để trống") MembershipStatus status) {
    }

    public record AuthorView(Long id, String username, String displayName) {
    }

    public record CategoryView(Long id, String name, String slug) {
    }

    public record CommentView(Long id, String content, AuthorView author, Instant createdAt) {
        public static CommentView from(Comment comment) {
            return new CommentView(comment.getId(), comment.getContent(),
                    new AuthorView(comment.getAuthor().getId(), comment.getAuthor().getUsername(),
                            comment.getAuthor().getDisplayName()), comment.getCreatedAt());
        }
    }

    public record MembershipView(Long id, Long postId, Long userId, String username, String displayName,
                                 String message, String contactInfo, MembershipStatus status,
                                 Instant createdAt) {
        public static MembershipView from(GroupMembership m) {
            return new MembershipView(m.getId(), m.getPost().getId(), m.getUser().getId(),
                    m.getUser().getUsername(), m.getUser().getDisplayName(),
                    m.getMessage(), m.getContactInfo(), m.getStatus(), m.getCreatedAt());
        }
    }

    public record PostView(Long id, String title, String content, PostStatus status,
                           Integer targetMembers, long acceptedMemberCount,
                           CategoryView category, AuthorView author, Instant createdAt, Instant updatedAt,
                           long reactionCount, long commentCount, boolean reactedByCurrentUser,
                           MembershipView myMembership,
                           List<MembershipView> memberships,
                           List<CommentView> comments) {
    }
}
