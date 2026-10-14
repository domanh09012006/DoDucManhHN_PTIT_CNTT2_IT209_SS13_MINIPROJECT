const API_URL = import.meta.env.VITE_API_URL || '/api'

let credentials = sessionStorage.getItem('campusHubCredentials') || ''

export function setCredentials(username, password) {
  try {
    const str = `${username}:${password}`
    credentials = btoa(unescape(encodeURIComponent(str)))
  } catch {
    credentials = btoa(`${username}:${password}`)
  }
  sessionStorage.setItem('campusHubCredentials', credentials)
}

export function clearCredentials() {
  credentials = ''
  sessionStorage.removeItem('campusHubCredentials')
}

export async function api(path, options = {}) {
  const headers = { ...options.headers }
  if (options.body) headers['Content-Type'] = 'application/json'

  // Không gửi header Authorization khi đăng ký tài khoản mới để tránh bị 401 do credentials cũ
  if (credentials && !path.startsWith('/auth/register') && !options.skipAuth) {
    headers.Authorization = `Basic ${credentials}`
  }

  const response = await fetch(`${API_URL}${path}`, { ...options, headers })
  if (response.status === 204) return null

  const text = await response.text()
  let body = {}
  try {
    body = text ? JSON.parse(text) : {}
  } catch {
    body = { message: text }
  }

  if (!response.ok) {
    let message = body.message || body.error
    if (!message || typeof message !== 'string' || message.trim() === '') {
      if (response.status === 401) message = 'Tài khoản hoặc mật khẩu không chính xác'
      else if (response.status === 403) message = 'Bạn không có quyền thực hiện thao tác này'
      else if (response.status === 409) message = 'Tên đăng nhập đã được sử dụng'
      else message = 'Không thể kết nối tới hệ thống'
    }
    throw new Error(message)
  }
  return body
}
