# Campus Hub Base

Campus Hub là dự án nền cho Mini Project Session 13. Ứng dụng cung cấp một không gian chung để sinh viên đăng sự kiện, tìm đồ thất lạc, hỏi đáp, trao đổi đồ dùng và tìm nhóm.

Dự án được giữ ở mức nhỏ để dễ đọc và sửa đổi, nhưng đã có đủ luồng giao diện, API, xác thực, migration và kiểm thử.

## Chức năng có sẵn

- Xem, tìm kiếm và lọc bài đăng.
- Đăng ký, đăng nhập bằng HTTP Basic.
- Tạo bài đăng theo chuyên mục.
- Bình luận và bày tỏ quan tâm.
- **[Mới - Mini Project] Tuyển thành viên & Tìm nhóm học tập**: Chủ bài đăng có thể đặt số lượng thành viên cần tìm; sinh viên khác gửi đơn ứng tuyển kèm lời nhắn & thông tin liên hệ; chủ bài có giao diện duyệt đơn (Chấp nhận / Từ chối). Hệ thống tự động hoàn tất bài khi đủ quân số.
- Chủ bài đăng có thể đánh dấu bài đã hoàn tất.
- Quản trị viên có quyền quản lý trạng thái bài đăng qua API.
- Health check tại `/actuator/health`.

Tài khoản mẫu được tạo khi ứng dụng khởi động lần đầu:

| Vai trò | Tên đăng nhập | Mật khẩu |
|---|---|---|
| Sinh viên | `student` | `student123` |
| Quản trị viên | `admin` | `admin123` |

Các tài khoản này chỉ dùng để trình diễn. Nhóm cần thay đổi hoặc loại bỏ trước khi sử dụng trong bối cảnh thực tế.

## Kiến trúc

```text
React frontend (Nginx Port 80)
    │ /api (Reverse proxy)
    ▼
Spring Boot monolith (Java 21 Port 8080)
    │ JDBC / Flyway
    ▼
MySQL (Port 3306)
```

## Chạy dự án bằng Docker Compose (Khuyên dùng)

Dự án đã được đóng gói hoàn chỉnh bằng Docker và Docker Compose gồm 3 services (`mysql`, `backend`, `frontend`):

```powershell
# Sao chép file cấu hình mẫu
copy .env.example .env

# Khởi động toàn bộ hệ thống
docker compose up --build -d
```

Sau khi chạy:
- Frontend truy cập tại: `http://localhost`
- Backend API truy cập tại: `http://localhost:8080/api`
- Health check: `http://localhost:8080/actuator/health`

Để dừng hệ thống:
```powershell
docker compose down
```

## Chạy khi phát triển cục bộ

Tạo database MySQL tên `campus_hub`, sau đó đặt các biến môi trường:

```powershell
$env:DB_URL = "jdbc:mysql://localhost:3306/campus_hub?createDatabaseIfNotExist=true"
$env:DB_USERNAME = "root"
$env:DB_PASSWORD = "your-password"
```

Chạy backend:

```powershell
cd backend
./gradlew.bat bootRun
```

Mở terminal khác để chạy frontend:

```powershell
cd frontend
npm install
npm run dev
```

Frontend phát triển chạy tại `http://localhost:5173` và chuyển tiếp `/api` tới backend tại cổng `8080`.

## Danh sách API

| Phương thức | Đường dẫn | Mục đích | Xác thực |
|---|---|---|---|
| `POST` | `/api/auth/register` | Tạo tài khoản | Không |
| `GET` | `/api/auth/me` | Lấy người dùng hiện tại | Có |
| `GET` | `/api/categories` | Danh sách chuyên mục | Không |
| `GET` | `/api/posts` | Tìm và lọc bài đăng | Không |
| `GET` | `/api/posts/{id}` | Chi tiết bài đăng | Không |
| `POST` | `/api/posts` | Tạo bài đăng (có hỗ trợ `targetMembers`) | Có |
| `PUT` | `/api/posts/{id}` | Sửa bài của mình | Có |
| `PATCH` | `/api/posts/{id}/status` | Đổi trạng thái bài | Có |
| `DELETE` | `/api/posts/{id}` | Xóa bài của mình | Có |
| `POST` | `/api/posts/{id}/comments` | Thêm bình luận | Có |
| `POST` | `/api/posts/{id}/reaction` | Bật hoặc tắt quan tâm | Có |
| **`POST`** | **`/api/posts/{id}/memberships`** | **Ứng tuyển vào nhóm (lời nhắn & liên hệ)** | **Có** |
| **`DELETE`** | **`/api/posts/{id}/memberships/me`** | **Huỷ đơn ứng tuyển của mình** | **Có** |
| **`PATCH`** | **`/api/posts/{id}/memberships/{mId}/status`** | **Chủ bài duyệt đơn (`ACCEPTED`/`REJECTED`)** | **Có** |
| **`GET`** | **`/api/posts/{id}/memberships`** | **Xem danh sách đơn ứng tuyển** | **Có** |

## Kiểm tra trước khi bàn giao (CI / Testing)

```powershell
cd backend
./gradlew.bat test

cd ../frontend
npm ci
npm run lint
npm run build
```

Hệ thống đã tích hợp sẵn GitHub Actions workflow tại [`.github/workflows/ci.yml`](.github/workflows/ci.yml) để tự động hóa kiểm thử mã nguồn và đóng gói Docker image mỗi khi đẩy commit lên nhánh `main`.
