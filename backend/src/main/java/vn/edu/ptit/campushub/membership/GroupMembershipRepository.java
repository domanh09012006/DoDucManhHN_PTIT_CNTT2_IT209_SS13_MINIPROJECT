package vn.edu.ptit.campushub.membership;

import java.util.List;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;

public interface GroupMembershipRepository extends JpaRepository<GroupMembership, Long> {
    List<GroupMembership> findByPostIdOrderByCreatedAtDesc(Long postId);

    Optional<GroupMembership> findByPostIdAndUserId(Long postId, Long userId);

    long countByPostIdAndStatus(Long postId, MembershipStatus status);

    void deleteByPostId(Long postId);
}
