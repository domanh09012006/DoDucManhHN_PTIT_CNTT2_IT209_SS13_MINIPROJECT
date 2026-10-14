import { useCallback, useEffect, useState } from 'react'
import { api, clearCredentials, setCredentials } from './api.js'

const emptyPost = { title: '', content: '', categoryId: '', targetMembers: '' }

function formatDate(value) {
  return new Intl.DateTimeFormat('vi-VN', { dateStyle: 'medium', timeStyle: 'short' }).format(new Date(value))
}

function App() {
  const [user, setUser] = useState(null)
  const [categories, setCategories] = useState([])
  const [posts, setPosts] = useState([])
  const [selectedPost, setSelectedPost] = useState(null)
  const [filters, setFilters] = useState({ keyword: '', categoryId: '' })
  const [dialog, setDialog] = useState(null)
  const [notice, setNotice] = useState('')

  const loadPosts = useCallback(async () => {
    const query = new URLSearchParams()
    if (filters.keyword) query.set('keyword', filters.keyword)
    if (filters.categoryId) query.set('categoryId', filters.categoryId)
    try {
      const page = await api(`/posts?${query}`)
      setPosts(page.content)
    } catch (error) {
      setNotice(error.message)
    }
  }, [filters])

  useEffect(() => {
    api('/categories').then(setCategories).catch((error) => setNotice(error.message))
    api('/auth/me').then(setUser).catch(() => clearCredentials())
  }, [])

  useEffect(() => {
    const query = new URLSearchParams()
    if (filters.keyword) query.set('keyword', filters.keyword)
    if (filters.categoryId) query.set('categoryId', filters.categoryId)
    let active = true
    api(`/posts?${query}`)
      .then((page) => { if (active) setPosts(page.content) })
      .catch((error) => { if (active) setNotice(error.message) })
    return () => { active = false }
  }, [filters])

  async function openPost(id) {
    try {
      setSelectedPost(await api(`/posts/${id}`))
    } catch (error) {
      setNotice(error.message)
    }
  }

  function logout() {
    clearCredentials()
    setUser(null)
    setSelectedPost(null)
    setNotice('Đã đăng xuất')
  }

  async function refreshSelected() {
    if (selectedPost) await openPost(selectedPost.id)
    await loadPosts()
  }

  return (
    <div className="app-shell">
      <header className="topbar">
        <button className="brand" onClick={() => setSelectedPost(null)}>
          <span className="brand-mark">C</span>
          <span>Campus Hub</span>
        </button>
        <nav>
          {user ? (
            <>
              <span className="user-name">Xin chào, {user.displayName}</span>
              <button className="button ghost" onClick={() => setDialog('post')}>Đăng bài</button>
              <button className="button secondary" onClick={logout}>Đăng xuất</button>
            </>
          ) : (
            <button className="button primary" onClick={() => setDialog('login')}>Đăng nhập</button>
          )}
        </nav>
      </header>

      <main>
        {notice && <div className="notice" onClick={() => setNotice('')}>{notice}</div>}
        {selectedPost ? (
          <PostDetail post={selectedPost} user={user} onBack={() => setSelectedPost(null)}
            onChanged={refreshSelected} onDeleted={() => { setSelectedPost(null); loadPosts() }}
            setNotice={setNotice} />
        ) : (
          <>
            <section className="hero">
              <div>
                <p className="eyebrow">Không gian chung của sinh viên</p>
                <h1>Chia sẻ điều đang diễn ra trong trường.</h1>
                <p>Tìm sự kiện, hỏi đáp, trao đổi đồ dùng và cùng kết nối tìm nhóm học tập.</p>
              </div>
              <div className="hero-stat"><strong>{posts.length}</strong><span>bài đăng đang hiển thị</span></div>
            </section>

            <section className="filters" aria-label="Tìm kiếm bài đăng">
              <input value={filters.keyword} placeholder="Tìm theo tiêu đề hoặc nội dung..."
                onChange={(event) => setFilters({ ...filters, keyword: event.target.value })} />
              <select value={filters.categoryId}
                onChange={(event) => setFilters({ ...filters, categoryId: event.target.value })}>
                <option value="">Tất cả chuyên mục</option>
                {categories.map((category) => <option key={category.id} value={category.id}>{category.name}</option>)}
              </select>
            </section>

            <section className="post-grid">
              {posts.map((post) => <PostCard key={post.id} post={post} onOpen={openPost} />)}
              {!posts.length && <div className="empty">Chưa có bài đăng phù hợp.</div>}
            </section>
          </>
        )}
      </main>

      <footer>Campus Hub · Dự án Mini Project DevOps Session 13</footer>

      {dialog === 'login' && <AuthDialog onClose={() => setDialog(null)} onLogin={(loggedInUser) => {
        setUser(loggedInUser); setDialog(null); setNotice('Đăng nhập thành công'); loadPosts()
      }} />}
      {dialog === 'post' && <PostDialog categories={categories} onClose={() => setDialog(null)}
        onSaved={() => { setDialog(null); setNotice('Đã đăng bài'); loadPosts() }} />}
    </div>
  )
}

function PostCard({ post, onOpen }) {
  return (
    <article className="post-card" onClick={() => onOpen(post.id)}>
      <div className="card-top">
        <span className="tag">{post.category.name}</span>
        {post.targetMembers && (
          <span className={`badge-group ${post.acceptedMemberCount >= post.targetMembers ? 'full' : ''}`}>
            👥 {post.acceptedMemberCount}/{post.targetMembers} người
          </span>
        )}
        <span>{formatDate(post.createdAt)}</span>
      </div>
      <h2>{post.title}</h2>
      <p>{post.content}</p>
      <div className="card-footer">
        <span>{post.author.displayName}</span>
        <span>♥ {post.reactionCount} · {post.commentCount} bình luận</span>
      </div>
    </article>
  )
}

function PostDetail({ post, user, onBack, onChanged, onDeleted, setNotice }) {
  const [comment, setComment] = useState('')
  const [applyOpen, setApplyOpen] = useState(false)
  const canManage = user && (user.id === post.author.id || user.role === 'ADMIN')
  const isAuthor = user && user.id === post.author.id

  async function act(action, success) {
    try {
      await action()
      setNotice(success)
      await onChanged()
    } catch (error) {
      setNotice(error.message)
    }
  }

  return (
    <section className="detail">
      <button className="back" onClick={onBack}>← Quay lại danh sách</button>
      <div className="detail-card">
        <div className="card-top">
          <span className="tag">{post.category.name}</span>
          {post.targetMembers && (
            <span className={`badge-group ${post.acceptedMemberCount >= post.targetMembers ? 'full' : ''}`}>
              👥 Đang tuyển nhóm ({post.acceptedMemberCount}/{post.targetMembers} người)
            </span>
          )}
          <span>{formatDate(post.createdAt)}</span>
        </div>
        <h1>{post.title}</h1>
        <p className="author">Đăng bởi {post.author.displayName} · Trạng thái: {post.status}</p>

        {post.targetMembers && (
          <div className="group-progress-box">
            <div className="group-progress-header">
              <strong>Tiến độ tuyển nhóm: {post.acceptedMemberCount} / {post.targetMembers} thành viên</strong>
              <span>{post.acceptedMemberCount >= post.targetMembers ? '🎉 Đã đủ thành viên' : 'Đang tìm kiếm thêm'}</span>
            </div>
            <div className="group-progress-bar">
              <div className="group-progress-fill"
                style={{ width: `${Math.min(100, Math.round((post.acceptedMemberCount / post.targetMembers) * 100))}%` }} />
            </div>
          </div>
        )}

        <div className="content">{post.content}</div>

        {/* Khối hiển thị trạng thái đơn ứng tuyển của sinh viên */}
        {user && !isAuthor && post.targetMembers && post.myMembership && (
          <div className="my-application-box">
            <div className="membership-item-header">
              <h3>Đơn đăng ký tham gia nhóm của bạn</h3>
              <span className={`status-badge ${post.myMembership.status}`}>
                {post.myMembership.status === 'PENDING' && 'Đang chờ duyệt ⏳'}
                {post.myMembership.status === 'ACCEPTED' && 'Đã được duyệt 🎉'}
                {post.myMembership.status === 'REJECTED' && 'Đã bị từ chối ❌'}
              </span>
            </div>
            <p className="membership-message"><strong>Lời nhắn:</strong> {post.myMembership.message}</p>
            <p><span className="membership-contact">Thông tin liên hệ đã gửi: {post.myMembership.contactInfo}</span></p>
            {post.myMembership.status === 'PENDING' && (
              <button className="button danger" style={{ marginTop: 10 }}
                onClick={() => act(() => api(`/posts/${post.id}/memberships/me`, { method: 'DELETE' }), 'Đã huỷ đơn đăng ký')}>
                Huỷ yêu cầu
              </button>
            )}
          </div>
        )}

        <div className="actions">
          <button className={`button ${post.reactedByCurrentUser ? 'primary' : 'secondary'}`} disabled={!user}
            onClick={() => act(() => api(`/posts/${post.id}/reaction`, { method: 'POST' }), 'Đã cập nhật quan tâm')}>
            ♥ {post.reactionCount} quan tâm
          </button>

          {/* Nút ứng tuyển cho sinh viên khác khi nhóm chưa đủ */}
          {user && !isAuthor && post.targetMembers && !post.myMembership && post.status === 'PUBLISHED' && post.acceptedMemberCount < post.targetMembers && (
            <button className="button primary" onClick={() => setApplyOpen(true)}>
              ✋ Đăng ký tham gia nhóm
            </button>
          )}

          {canManage && post.status !== 'RESOLVED' && <button className="button secondary"
            onClick={() => act(() => api(`/posts/${post.id}/status`, {
              method: 'PATCH', body: JSON.stringify({ status: 'RESOLVED' }),
            }), 'Đã đánh dấu hoàn tất')}>Đánh dấu hoàn tất</button>}
          {user?.role === 'ADMIN' && post.status !== 'HIDDEN' && <button className="button secondary"
            onClick={() => act(() => api(`/posts/${post.id}/status`, {
              method: 'PATCH', body: JSON.stringify({ status: 'HIDDEN' }),
            }), 'Đã ẩn bài đăng')}>Ẩn bài</button>}
          {canManage && <button className="button danger" onClick={async () => {
            if (!window.confirm('Xóa bài đăng này?')) return
            try {
              await api(`/posts/${post.id}`, { method: 'DELETE' })
              setNotice('Đã xóa bài đăng')
              onDeleted()
            } catch (error) {
              setNotice(error.message)
            }
          }}>Xóa bài</button>}
        </div>
      </div>

      {/* Quản lý danh sách ứng viên (Dành riêng cho chủ bài viết hoặc ADMIN) */}
      {canManage && post.targetMembers && post.memberships && (
        <div className="membership-box">
          <h2>Danh sách ứng viên đăng ký tham gia ({post.memberships.length})</h2>
          {post.memberships.length === 0 ? (
            <p className="muted">Chưa có sinh viên nào gửi yêu cầu tham gia.</p>
          ) : (
            <div className="membership-list">
              {post.memberships.map((m) => (
                <div key={m.id} className="membership-item">
                  <div className="membership-item-header">
                    <div>
                      <span className="membership-user">{m.displayName} (@{m.username})</span>
                      <span className="membership-meta"> · {formatDate(m.createdAt)}</span>
                    </div>
                    <span className={`status-badge ${m.status}`}>
                      {m.status === 'PENDING' && 'Chờ duyệt'}
                      {m.status === 'ACCEPTED' && 'Đã duyệt'}
                      {m.status === 'REJECTED' && 'Từ chối'}
                    </span>
                  </div>
                  <p className="membership-message">"{m.message}"</p>
                  <div><span className="membership-contact">Liên hệ: {m.contactInfo}</span></div>
                  {m.status === 'PENDING' && (
                    <div className="membership-actions">
                      <button className="button primary" onClick={() => act(() => api(`/posts/${post.id}/memberships/${m.id}/status`, {
                        method: 'PATCH', body: JSON.stringify({ status: 'ACCEPTED' })
                      }), 'Đã chấp nhận thành viên')}>
                        ✓ Chấp nhận
                      </button>
                      <button className="button secondary" onClick={() => act(() => api(`/posts/${post.id}/memberships/${m.id}/status`, {
                        method: 'PATCH', body: JSON.stringify({ status: 'REJECTED' })
                      }), 'Đã từ chối')}>
                        ✕ Từ chối
                      </button>
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      <div className="comments">
        <h2>Bình luận ({post.commentCount})</h2>
        {user ? <form onSubmit={(event) => {
          event.preventDefault()
          act(() => api(`/posts/${post.id}/comments`, { method: 'POST', body: JSON.stringify({ content: comment }) }),
            'Đã thêm bình luận').then(() => setComment(''))
        }}>
          <textarea value={comment} onChange={(event) => setComment(event.target.value)}
            placeholder="Viết bình luận..." required maxLength="1000" />
          <button className="button primary">Gửi bình luận</button>
        </form> : <p className="muted">Đăng nhập để bình luận, bày tỏ quan tâm hoặc đăng ký nhóm.</p>}
        <div className="comment-list">
          {post.comments.map((item) => <div className="comment" key={item.id}>
            <strong>{item.author.displayName}</strong><span>{formatDate(item.createdAt)}</span><p>{item.content}</p>
          </div>)}
        </div>
      </div>

      {applyOpen && (
        <ApplyDialog postId={post.id} onClose={() => setApplyOpen(false)}
          onApplied={() => { setApplyOpen(false); setNotice('Đã gửi đơn đăng ký tham gia nhóm!'); onChanged() }} />
      )}
    </section>
  )
}

function ApplyDialog({ postId, onClose, onApplied }) {
  const [form, setForm] = useState({ message: '', contactInfo: '' })
  const [error, setError] = useState('')

  async function submit(e) {
    e.preventDefault()
    try {
      await api(`/posts/${postId}/memberships`, { method: 'POST', body: JSON.stringify(form) })
      onApplied()
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <Dialog title="Đăng ký tham gia nhóm / hoạt động" onClose={onClose}>
      <form className="form" onSubmit={submit}>
        {error && <p className="form-error">{error}</p>}
        <label>
          Lời nhắn giới thiệu bản thân & lý do muốn tham gia
          <textarea required rows="4" maxLength="500" value={form.message}
            placeholder="Ví dụ: Mình là sinh viên lớp D24, muốn vào nhóm cùng làm bài tập lớn DevOps..."
            onChange={(e) => setForm({ ...form, message: e.target.value })} />
        </label>
        <label>
          Thông tin liên hệ (SĐT / Zalo / Facebook)
          <input required maxLength="100" value={form.contactInfo}
            placeholder="Ví dụ: SĐT/Zalo: 0987654321"
            onChange={(e) => setForm({ ...form, contactInfo: e.target.value })} />
        </label>
        <button className="button primary">Gửi yêu cầu tham gia</button>
      </form>
    </Dialog>
  )
}

function AuthDialog({ onClose, onLogin }) {
  const [mode, setMode] = useState('login')
  const [form, setForm] = useState({ username: '', displayName: '', password: '' })
  const [error, setError] = useState('')

  async function submit(event) {
    event.preventDefault()
    setError('')
    try {
      if (mode === 'register') {
        clearCredentials()
        await api('/auth/register', { method: 'POST', body: JSON.stringify(form) })
      }
      setCredentials(form.username, form.password)
      const loggedInUser = await api('/auth/me')
      onLogin(loggedInUser)
    } catch (requestError) {
      clearCredentials()
      setError(requestError.message)
    }
  }

  return <Dialog title={mode === 'login' ? 'Đăng nhập' : 'Tạo tài khoản'} onClose={onClose}>
    <form className="form" onSubmit={submit}>
      {error && <p className="form-error">{error}</p>}
      <label>Tên đăng nhập (chữ không dấu, số, viết liền)
        <input required minLength="3" maxLength="60" pattern="[a-zA-Z0-9._-]+"
          placeholder="Ví dụ: nguyenvana"
          title="Tên đăng nhập chỉ gồm chữ không dấu, số, dấu chấm, gạch ngang hoặc gạch dưới"
          value={form.username}
          onChange={(event) => {
            setError('')
            setForm({ ...form, username: event.target.value.toLowerCase().replace(/\s+/g, '') })
          }} />
      </label>
      {mode === 'register' && <label>Tên hiển thị
        <input required maxLength="100" placeholder="Ví dụ: Nguyễn Văn A"
          value={form.displayName}
          onChange={(event) => {
            setError('')
            setForm({ ...form, displayName: event.target.value })
          }} />
      </label>}
      <label>Mật khẩu (tối thiểu 6 ký tự)
        <input required minLength="6" maxLength="72" type="password" placeholder="••••••••"
          value={form.password}
          onChange={(event) => {
            setError('')
            setForm({ ...form, password: event.target.value })
          }} />
      </label>
      <button className="button primary">{mode === 'login' ? 'Đăng nhập' : 'Đăng ký'}</button>
      <button type="button" className="text-button" onClick={() => {
        setMode(mode === 'login' ? 'register' : 'login')
        setError('')
        clearCredentials()
      }}>
        {mode === 'login' ? 'Chưa có tài khoản? Đăng ký' : 'Đã có tài khoản? Đăng nhập'}
      </button>
    </form>
  </Dialog>
}

function PostDialog({ categories, onClose, onSaved }) {
  const [form, setForm] = useState(emptyPost)
  const [error, setError] = useState('')

  async function submit(event) {
    event.preventDefault()
    try {
      const payload = {
        title: form.title,
        content: form.content,
        categoryId: Number(form.categoryId),
        targetMembers: form.targetMembers ? Number(form.targetMembers) : null,
      }
      await api('/posts', { method: 'POST', body: JSON.stringify(payload) })
      onSaved()
    } catch (requestError) {
      setError(requestError.message)
    }
  }

  return <Dialog title="Tạo bài đăng" onClose={onClose}>
    <form className="form" onSubmit={submit}>
      {error && <p className="form-error">{error}</p>}
      <label>Tiêu đề<input required maxLength="160" value={form.title}
        onChange={(event) => setForm({ ...form, title: event.target.value })} /></label>
      <label>Chuyên mục<select required value={form.categoryId}
        onChange={(event) => setForm({ ...form, categoryId: event.target.value })}>
        <option value="">Chọn chuyên mục</option>
        {categories.map((category) => <option key={category.id} value={category.id}>{category.name}</option>)}
      </select></label>
      <label>Số lượng thành viên cần tìm (để trống nếu không tuyển nhóm)
        <input type="number" min="1" max="50" placeholder="Ví dụ: 3 thành viên" value={form.targetMembers}
          onChange={(event) => setForm({ ...form, targetMembers: event.target.value })} />
      </label>
      <label>Nội dung<textarea required maxLength="10000" rows="7" value={form.content}
        onChange={(event) => setForm({ ...form, content: event.target.value })} /></label>
      <button className="button primary">Đăng bài</button>
    </form>
  </Dialog>
}

function Dialog({ title, onClose, children }) {
  return <div className="dialog-backdrop" onMouseDown={onClose}>
    <section className="dialog" role="dialog" aria-modal="true" onMouseDown={(event) => event.stopPropagation()}>
      <div className="dialog-title"><h2>{title}</h2><button onClick={onClose} aria-label="Đóng">×</button></div>
      {children}
    </section>
  </div>
}

export default App
