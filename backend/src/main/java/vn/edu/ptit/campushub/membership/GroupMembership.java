package vn.edu.ptit.campushub.membership;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import jakarta.persistence.UniqueConstraint;
import java.time.Instant;
import vn.edu.ptit.campushub.post.Post;
import vn.edu.ptit.campushub.user.User;

@Entity
@Table(name = "group_memberships", uniqueConstraints = {
        @UniqueConstraint(name = "uk_membership_post_user", columnNames = {"post_id", "user_id"})
})
public class GroupMembership {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "post_id")
    private Post post;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "user_id")
    private User user;

    @Column(nullable = false, length = 500)
    private String message;

    @Column(nullable = false, length = 100)
    private String contactInfo;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false, length = 20)
    private MembershipStatus status = MembershipStatus.PENDING;

    @Column(nullable = false, updatable = false)
    private Instant createdAt;

    @Column(nullable = false)
    private Instant updatedAt;

    protected GroupMembership() {
    }

    public GroupMembership(Post post, User user, String message, String contactInfo) {
        this.post = post;
        this.user = user;
        this.message = message;
        this.contactInfo = contactInfo;
        this.status = MembershipStatus.PENDING;
        this.createdAt = Instant.now();
        this.updatedAt = this.createdAt;
    }

    public void updateStatus(MembershipStatus status) {
        this.status = status;
        this.updatedAt = Instant.now();
    }

    public Long getId() { return id; }
    public Post getPost() { return post; }
    public User getUser() { return user; }
    public String getMessage() { return message; }
    public String getContactInfo() { return contactInfo; }
    public MembershipStatus getStatus() { return status; }
    public Instant getCreatedAt() { return createdAt; }
    public Instant getUpdatedAt() { return updatedAt; }
}
