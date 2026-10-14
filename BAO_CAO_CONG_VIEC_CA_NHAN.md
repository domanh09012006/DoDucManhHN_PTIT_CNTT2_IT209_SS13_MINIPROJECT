# BÁO CÁO CÔNG VIỆC CÁ NHÂN — MINI PROJECT TỔNG HỢP (SESSION 13)

**Học phần:** DevOps (IT209)  
**Dự án:** Nâng cấp & Tự động hóa triển khai nền tảng Campus Hub (Tìm nhóm học tập sinh viên)  
**Nhóm thực hiện:** Nhóm DevOps Session 13 (Nhóm 04)  
**Họ và tên sinh viên:** Đỗ Đức Mạnh  
**Tài khoản Git / Email:** `domanh09012006` / `doducmanh09012006@gmail.com`  
**Vai trò phân công trong nhóm:** DevOps Engineer (Orchestration & CI/CD Pipeline)  

---

## 1. Giới thiệu ngắn gọn về dự án Campus Hub

Campus Hub là nền tảng chia sẻ thông tin trực tuyến trong môi trường đại học, kết nối sinh viên nhằm chia sẻ sự kiện, tìm đồ thất lạc, hỏi đáp học tập và giải quyết bài toán cấp thiết: **tìm kiếm bạn cùng nhóm để làm bài tập lớn, đồ án môn học và nghiên cứu khoa học**.

Dự án được xây dựng và nâng cấp từ mã nguồn nền **Campus Hub Base** (Spring Boot Java 21, React SPA, MySQL 8.4). Nhóm đã nâng cấp phân hệ nghiệp vụ **Tuyển thành viên & Quản lý đơn ứng tuyển nhóm học tập**, đồng thời hiện đại hóa toàn diện hạ tầng vận hành bằng công nghệ containerization (Docker, Docker Compose), Reverse Proxy (Nginx) và quy trình tự động hóa kiểm thử, đóng gói liên tục (CI/CD qua GitHub Actions).

---

## 2. Vai trò và phạm vi công việc cá nhân theo README phân công

Căn cứ theo tài liệu phân công nhiệm vụ của nhóm tại [README_KICH_BAN_DEMO_BAO_CAO.md](file:///d:/IT209/Session13_MiniProject_Nhom04-main/README_KICH_BAN_DEMO_BAO_CAO.md#L123-L139) và tài liệu tổng hợp tại [generate_report.py](file:///d:/IT209/Session13_MiniProject_Nhom04-main/generate_report.py#L156-L168), vai trò và phạm vi công việc được giao của tôi như sau:

- **Vị trí đảm nhiệm:** Thành viên số 9 — **DevOps Engineer (Orchestration & CI/CD)**.
- **Phạm vi trách nhiệm chính:**
  1. Xây dựng và tối ưu tệp điều phối đa dịch vụ [docker-compose.yml](file:///d:/IT209/Session13_MiniProject_Nhom04-main/docker-compose.yml) kết nối 3 thành phần: CSDL MySQL 8.4, Backend Spring Boot và Frontend Nginx.
  2. Thiết lập cơ chế kiểm tra sức khỏe phụ thuộc (`healthcheck`) cho database để loại trừ hoàn toàn hiện tượng race condition (Backend khởi động trước khi MySQL sẵn sàng nhận kết nối JDBC).
  3. Xây dựng đường ống tích hợp và kiểm thử liên tục (CI/CD Pipeline) bằng GitHub Actions tại [.github/workflows/ci.yml](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.github/workflows/ci.yml) nhằm tự động chạy test, linting, build ứng dụng và xác thực đóng gói Docker image mỗi khi có commit đẩy lên nhánh `main`.
  4. Quản lý biến môi trường, bảo vệ an toàn các thông tin nhạy cảm (secrets) theo tiêu chuẩn 12-Factor App ([.env.example](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.env.example), [.gitignore](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.gitignore)).
  5. Đảm nhiệm phần thuyết trình kỹ thuật về Hạ tầng Điều phối & CI/CD Pipeline (khung thời gian 24:00 - 27:00 trong kịch bản bảo vệ dự án).

---

## 3. Danh sách các công việc được giao

| STT | Tên công việc | Mục tiêu | Trạng thái ghi nhận |
| :---: | :--- | :--- | :---: |
| **CV-01** | Xây dựng tệp điều phối đa container `docker-compose.yml` | Khởi chạy toàn bộ hệ sinh thái (MySQL, Backend, Frontend) bằng một câu lệnh duy nhất, cấu hình mạng bridge nội bộ và volume lưu trữ bền vững. | **Đã hoàn thành** (Có mã nguồn kiểm chứng) |
| **CV-02** | Thiết lập cơ chế Healthcheck & Điều kiện khởi động phụ thuộc (`depends_on: condition: service_healthy`) | Đảm bảo tính tuần tự khi khởi động hệ thống: Backend chỉ start sau khi MySQL ping thành công, giải quyết triệt để lỗi Connection Refused. | **Đã hoàn thành** (Có mã nguồn kiểm chứng) |
| **CV-03** | Xây dựng CI/CD Pipeline tự động hóa với GitHub Actions (`.github/workflows/ci.yml`) | Tự động hóa kiểm thử mã nguồn backend (`./gradlew test`), kiểm tra cú pháp và build frontend (`npm run lint`, `npm run build`), xác thực build Docker image. | **Đã hoàn thành** (Có mã nguồn kiểm chứng) |
| **CV-04** | Quản lý cấu hình môi trường và bảo mật Secret theo tiêu chuẩn 12-Factor App | Tách biệt hoàn toàn cấu hình khỏi mã nguồn: tạo `.env.example`, đưa `.env` vào `.gitignore`, truyền biến an toàn vào container. | **Đã hoàn thành** (Có mã nguồn kiểm chứng) |
| **CV-05** | Chuẩn bị nội dung thuyết trình và trả lời phản biện về DevOps & CI/CD | Chuẩn bị slide, kịch bản báo cáo phần Orchestration & CI/CD, chuẩn bị câu trả lời phản biện về pipeline và Docker compose. | **Đã hoàn thành** (Có trong kịch bản demo) |

---

## 4. Mô tả chi tiết từng công việc và cách thực hiện

### 4.1. Công việc 1: Xây dựng tệp điều phối đa container `docker-compose.yml`
- **Mục tiêu:** Cho phép người dùng và giảng viên chấm bài khởi chạy toàn bộ hệ thống full-stack chỉ bằng một lệnh `docker compose up --build -d` mà không cần cài đặt cục bộ Java, Node.js hay MySQL trên máy chủ.
- **Nội dung thực hiện cụ thể:**
  - Định nghĩa 3 dịch vụ chính:
    1. `mysql`: Dùng image chính thức `mysql:8.4`, thiết lập cấu hình container name `campushub-mysql`, ánh xạ cổng `3306:3306`.
    2. `backend`: Thiết lập `build.context: ./backend`, sử dụng Dockerfile multi-stage sẵn có, ánh xạ cổng `8080:8080`, truyền các biến môi trường JDBC kết nối tới host `mysql` qua mạng nội bộ.
    3. `frontend`: Thiết lập `build.context: ./frontend`, ánh xạ cổng `80:80`, phụ thuộc vào service `backend`.
  - Cấu hình Volume bền vững `mysql_data:/var/lib/mysql` để bảo toàn dữ liệu bài viết, tài khoản và đơn ứng tuyển ngay cả khi container bị dừng hoặc xóa (`docker compose down`).
  - Thiết lập mạng nội bộ cô lập `campushub-network` (driver `bridge`) để các service liên lạc thông qua hostname của container.

### 4.2. Công việc 2: Cấu hình Healthcheck và quản lý phụ thuộc khởi động dịch vụ
- **Mục tiêu:** Ngăn chặn lỗi kinh điển trong các ứng dụng containerized khi Spring Boot khởi động nhanh hơn thời gian khởi tạo socket của MySQL, dẫn đến lỗi sập ứng dụng (`Communications link failure / Connection Refused`).
- **Nội dung thực hiện cụ thể:**
  - Cấu hình chỉ thị `healthcheck` cho dịch vụ `mysql`:
    - Sử dụng lệnh kiểm tra nội bộ: `["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-p$${MYSQL_ROOT_PASSWORD}"]`.
    - Thiết lập chu kỳ kiểm tra `interval: 10s`, thời gian chờ tối đa `timeout: 5s`, số lần thử lại trước khi đánh dấu lỗi `retries: 5`.
  - Trong dịch vụ `backend`, sử dụng chỉ thị:
    ```yaml
    depends_on:
      mysql:
        condition: service_healthy
    ```
  - Cơ chế này buộc Docker Compose phải chờ tới khi container MySQL trả về trạng thái `healthy` thì mới kích hoạt container Backend, đảm bảo Spring Boot kết nối CSDL và chạy Flyway migration thành công 100%.

### 4.3. Công việc 3: Xây dựng CI/CD Pipeline với GitHub Actions
- **Mục tiêu:** Xây dựng quy trình tích hợp liên tục tự động kiểm thử và thẩm định chất lượng mã nguồn mỗi khi có thay đổi được đẩy lên nhánh chính (`main`).
- **Nội dung thực hiện cụ thể:**
  - Tạo tệp cấu hình [.github/workflows/ci.yml](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.github/workflows/ci.yml).
  - Cấu hình điều kiện kích hoạt: sự kiện `push` và `pull_request` vào nhánh `main`.
  - Thiết lập 3 jobs rõ ràng:
    1. **Job `backend-test` (Backend Tests & Build):**
       - Môi trường: `ubuntu-latest`.
       - Setup JDK 21 (Eclipse Temurin) kèm cơ chế cache Gradle.
       - Cấp quyền thực thi cho Gradle wrapper: `chmod +x backend/gradlew`.
       - Chạy toàn bộ kiểm thử Unit Test và Integration Test: `./gradlew test` (kiểm tra tính toàn vẹn của logic nghiệp vụ).
       - Đóng gói file chạy ứng dụng: `./gradlew bootJar -x test`.
    2. **Job `frontend-check` (Frontend Lint & Build):**
       - Môi trường: `ubuntu-latest`.
       - Setup Node.js phiên bản 20 kèm cache npm.
       - Cài đặt dependency chuẩn: `npm ci`.
       - Kiểm tra chuẩn mực cú pháp và lỗi tiềm ẩn: `npm run lint`.
       - Biên dịch gói tĩnh: `npm run build`.
    3. **Job `docker-build-verify` (Docker Build Verification):**
       - Điều kiện phụ thuộc: `needs: [backend-test, frontend-check]`.
       - Khởi tạo Docker Buildx (`actions/setup-buildx-action@v3`).
       - Thực thi đóng gói thử nghiệm `campushub-backend:latest` và `campushub-frontend:latest` để đảm bảo các tệp Dockerfile không bị lỗi cú pháp hay thiếu tệp đầu vào khi chuyển giao sang môi trường production.

### 4.4. Công việc 4: Quản lý biến môi trường và bảo mật Secret
- **Mục tiêu:** Đảm bảo tuân thủ nguyên tắc cấu hình của 12-Factor App và yêu cầu bảo mật thông tin trong môn học DevOps (không hard-code mật khẩu và thông tin nhạy cảm vào mã nguồn công khai).
- **Nội dung thực hiện cụ thể:**
  - Khởi tạo tệp mẫu [.env.example](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.env.example) mô tả các biến cần thiết: `DB_NAME`, `DB_PASSWORD`, `SERVER_PORT`.
  - Kiểm tra và đảm bảo tệp cấu hình [.gitignore](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.gitignore) đã khai báo `.env` ở dòng đầu tiên, tuyệt đối không đưa thông tin nhạy cảm lên Git.
  - Áp dụng kỹ thuật biến môi trường có giá trị mặc định dự phòng trong [docker-compose.yml](file:///d:/IT209/Session13_MiniProject_Nhom04-main/docker-compose.yml): ví dụ `${DB_PASSWORD:-password123}`, giúp hệ thống vẫn có thể khởi động kiểm thử thuận tiện nếu người dùng chưa kịp tùy biến file `.env`.

### 4.5. Công việc 5: Chuẩn bị kịch bản thuyết trình bảo vệ phần Orchestration & CI/CD
- **Mục tiêu:** Trình bày rõ ràng giải pháp hạ tầng trong buổi bảo vệ trước Giảng viên và Hội đồng.
- **Nội dung thực hiện cụ thể:**
  - Đóng góp nội dung cho [README_KICH_BAN_DEMO_BAO_CAO.md](file:///d:/IT209/Session13_MiniProject_Nhom04-main/README_KICH_BAN_DEMO_BAO_CAO.md#L137): phụ trách lượt nói từ phút 24:00 đến 27:00 (trình bày điều phối `docker-compose.yml`, cơ chế healthcheck của MySQL và quy trình CI/CD qua GitHub Actions).
  - Chuẩn bị nội dung trả lời cho **Câu hỏi phản biện số 5** của Giảng viên: *"Quy trình CI/CD qua GitHub Actions của nhóm hoạt động như thế nào?"*.

---

## 5. Các file, chức năng hoặc thành phần liên quan

Dưới đây là các tệp tin trong dự án mà tôi trực tiếp tạo lập, cấu hình hoặc có liên quan mật thiết đến phạm vi công việc cá nhân:

| Đường dẫn tệp tin | Vai trò / Thành phần | Nội dung chi tiết |
| :--- | :--- | :--- |
| [docker-compose.yml](file:///d:/IT209/Session13_MiniProject_Nhom04-main/docker-compose.yml) | Hạ tầng điều phối (Orchestration) | Khai báo 3 services (`mysql`, `backend`, `frontend`), cấu hình port forwarding, bridge network, volume `mysql_data`, và block `healthcheck`. |
| [.github/workflows/ci.yml](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.github/workflows/ci.yml) | Đường ống CI/CD (Pipeline) | Thiết lập pipeline GitHub Actions gồm 3 jobs: `backend-test`, `frontend-check`, `docker-build-verify`. |
| [.env.example](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.env.example) | Quản lý cấu hình mẫu | Cung cấp template khai báo biến môi trường cho môi trường Docker Compose và Production. |
| [.gitignore](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.gitignore) | Bảo mật mã nguồn | Khai báo loại trừ `.env` để ngăn chặn lộ thông tin mật khẩu kết nối CSDL lên repository. |
| [README_KICH_BAN_DEMO_BAO_CAO.md](file:///d:/IT209/Session13_MiniProject_Nhom04-main/README_KICH_BAN_DEMO_BAO_CAO.md#L137) | Kịch bản báo cáo bảo vệ | Phân công vai trò thuyết trình của Đỗ Đức Mạnh (phút 24:00 - 27:00) và câu hỏi phản biện CI/CD số 5. |
| [generate_report.py](file:///d:/IT209/Session13_MiniProject_Nhom04-main/generate_report.py#L165) | Báo cáo đồ án nhóm | Bảng phân công ghi nhận đóng góp 100% cho vị trí DevOps Engineer (Orchestration & CI/CD). |

---

## 6. Kết quả thực tế và bằng chứng kiểm chứng được

Các kết quả công việc đã hoàn thành đều có bằng chứng cụ thể, có thể kiểm chứng trực tiếp trong mã nguồn và môi trường thực thi:

### 6.1. Bằng chứng về `docker-compose.yml`
- Tệp [docker-compose.yml](file:///d:/IT209/Session13_MiniProject_Nhom04-main/docker-compose.yml) có dung lượng 1,437 bytes, gồm 62 dòng lệnh chuẩn cú pháp Compose Spec v3.8.
- Cấu hình healthcheck chính xác:
  ```yaml
  healthcheck:
    test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-p$${MYSQL_ROOT_PASSWORD}"]
    interval: 10s
    timeout: 5s
    retries: 5
  ```
- Backend phụ thuộc có điều kiện: `condition: service_healthy`.
- Volume `mysql_data` và network `campushub-network` được khai báo đầy đủ ở cấp độ root của tệp Compose.

### 6.2. Bằng chứng về pipeline CI/CD GitHub Actions
- Tệp [.github/workflows/ci.yml](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.github/workflows/ci.yml) có dung lượng 1,885 bytes, gồm 80 dòng lệnh cấu hình rõ ràng.
- Đầy đủ các bước kiểm thử tự động quan trọng:
  - Backend: `./gradlew test` (thực thi kiểm thử MockMvc và API integration test).
  - Frontend: `npm run lint` và `npm run build`.
  - Docker: `docker build -t campushub-backend:latest ./backend` và `docker build -t campushub-frontend:latest ./frontend`.
- Thiết lập cơ chế phụ thuộc `needs: [backend-test, frontend-check]` ngăn chặn việc lãng phí tài nguyên build image khi mã nguồn chưa vượt qua các bài kiểm thử chất lượng.

### 6.3. Bằng chứng về bảo mật và biến môi trường
- Tệp [.gitignore](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.gitignore) dòng số 1 đã chứa `.env`.
- Tệp [.env.example](file:///d:/IT209/Session13_MiniProject_Nhom04-main/.env.example) có cấu trúc mạch lạc, hướng dẫn người dùng tạo file `.env` trước khi chạy `docker compose up --build -d`.

---

## 7. Đối chiếu công việc cá nhân với yêu cầu đề bài Session 13

Đề bài Session 13 — Mini Project Tổng hợp học phần DevOps đặt ra các tiêu chuẩn khắt khe về kiến trúc, kiểm thử và tự động hóa vận hành. Dưới đây là bảng đối chiếu chi tiết:

| Tiêu chí đề bài Session 13 | Nội dung yêu cầu | Mức độ đáp ứng trong phần việc của cá nhân |
| :--- | :--- | :--- |
| **Đóng gói & Điều phối đa dịch vụ (Orchestration)** | Cung cấp giải pháp chạy hệ thống đa dịch vụ đồng bộ, dễ triển khai, có quản lý dữ liệu lưu trữ bền vững. | **Đáp ứng 100%:** Thiết kế `docker-compose.yml` tích hợp 3 services, cấu hình Named Volume `mysql_data` và bridge network biệt lập. |
| **Độ tin cậy & Sẵn sàng của dịch vụ (Reliability & Healthcheck)** | Tránh lỗi xung đột thời gian khởi động giữa CSDL và Web Server; có cơ chế giám sát sức khỏe dịch vụ. | **Đáp ứng 100%:** Triển khai `healthcheck` qua `mysqladmin ping` và liên kết với `condition: service_healthy` cho backend. |
| **Quy trình Tích hợp liên tục (CI/CD Pipeline)** | Thiết lập pipeline tự động hóa quy trình kiểm thử mã nguồn và xác thực đóng gói ứng dụng. | **Đáp ứng 100%:** Xây dựng workflow GitHub Actions hoàn chỉnh với 3 jobs (test backend, lint & build frontend, build docker images). |
| **Quản lý cấu hình & Bảo mật Secrets** | Tuân thủ tiêu chuẩn 12-Factor App, không lưu trữ thông tin nhạy cảm trực tiếp trong kho mã nguồn. | **Đáp ứng 100%:** Cung cấp `.env.example`, đưa `.env` vào `.gitignore` và nạp biến động qua Docker Compose. |
| **Tài liệu hóa & Báo cáo bảo vệ** | Có kịch bản hướng dẫn chạy hệ thống rõ ràng, chuẩn bị nội dung thuyết trình phân công theo vai trò. | **Đáp ứng 100%:** Đóng góp kịch bản khởi chạy và phân đoạn thuyết trình kỹ thuật trong [README_KICH_BAN_DEMO_BAO_CAO.md](file:///d:/IT209/Session13_MiniProject_Nhom04-main/README_KICH_BAN_DEMO_BAO_CAO.md). |

---

## 8. Những vấn đề gặp phải và cách xử lý

Trong quá trình xây dựng hạ tầng Docker Compose và GitHub Actions, tôi đã gặp và xử lý các vấn đề kỹ thuật thực tế sau:

1. **Lỗi Race Condition giữa MySQL và Spring Boot:**
   - *Vấn đề:* Mặc định chỉ thị `depends_on: - mysql` trong Docker Compose chỉ chờ container MySQL được tạo và khởi chạy tiến trình, chứ không chờ dịch vụ MySQL mở cổng và sẵn sàng nhận kết nối socket. Khi Spring Boot khởi động sớm hơn, ứng dụng sẽ văng ngoại lệ `Communications link failure` và thoát tiến trình.
   - *Cách xử lý:* Bổ sung khối `healthcheck` cho service `mysql` sử dụng công cụ `mysqladmin ping`, đồng thời cấu hình lại `backend` sử dụng `condition: service_healthy`. Nhờ vậy, backend chỉ khởi chạy khi MySQL thực sự sẵn sàng.

2. **Xử lý cú pháp biến môi trường kép trong Healthcheck:**
   - *Vấn đề:* Trong cú pháp Docker Compose, ký tự `$` đơn được hiểu là nội suy biến của Compose. Khi chạy lệnh kiểm tra mật khẩu `-p$MYSQL_ROOT_PASSWORD`, lệnh có thể bị đọc nhầm biến rỗng.
   - *Cách xử lý:* Sử dụng cú pháp escape `$$` (`-p$${MYSQL_ROOT_PASSWORD}`) trong khai báo lệnh test healthcheck để Docker truyền chính xác biến môi trường vào container shell.

3. **Tối ưu hóa thời gian chạy và thứ tự thực thi của CI Pipeline:**
   - *Vấn đề:* Nếu chạy tuần tự từng bước từ backend đến frontend rồi mới đóng gói Docker, thời gian chạy workflow có thể kéo dài; ngược lại nếu build Docker ngay từ đầu mà mã nguồn có lỗi logic thì gây lãng phí tài nguyên máy ảo GitHub.
   - *Cách xử lý:* Thiết kế job `backend-test` và `frontend-check` chạy độc lập, sau đó cấu hình job `docker-build-verify` phụ thuộc vào cả 2 job thông qua `needs: [backend-test, frontend-check]`. Bật cơ chế cache (`cache: 'gradle'` và `cache: 'npm'`) để tăng tốc độ thực thi pipeline.

---

## 9. Những công việc chưa hoàn thành hoặc còn cần xác minh

- **Trạng thái thực tế của GitHub Actions trên remote repository:** Tệp cấu hình `.github/workflows/ci.yml` đã được viết và kiểm tra chuẩn cú pháp hoàn chỉnh trong workspace cục bộ. Tuy nhiên, do thư mục hiện tại là bản snapshot mã nguồn (không chứa thư mục `.git`), trạng thái kích hoạt thực tế (pass/fail badges) của pipeline cần được xác minh trực tiếp trên giao diện web của GitHub repository khi nhóm đồng bộ mã nguồn lên remote.
- **Môi trường chạy Docker Compose:** Để thực thi lệnh `docker compose up --build -d` trong quá trình demo bảo vệ trên máy chiếu, máy tính thực hiện demo bắt buộc phải cài đặt và khởi động sẵn Docker Desktop (hoặc Docker Engine). Kịch bản dự phòng chạy thủ công bằng lệnh dev cục bộ (`./gradlew.bat bootRun` và `npm run dev`) đã được nhóm ghi rõ trong tài liệu kịch bản để tránh rủi ro kỹ thuật.

---

## 10. Tóm tắt đóng góp cá nhân vào sản phẩm nhóm

- **Đóng góp về mặt hạ tầng:** Đã hoàn thành 100% nhiệm vụ xây dựng hệ sinh thái điều phối container bằng Docker Compose, giúp việc triển khai dự án Campus Hub trở nên nhất quán, loại bỏ hoàn toàn các lỗi sai khác môi trường (Java version, Node version, cấu hình port) giữa máy tính của các thành viên và máy chấm thi.
- **Đóng góp về mặt tự động hóa (DevOps):** Thiết lập pipeline CI/CD tự động trên GitHub Actions bảo vệ chất lượng nhánh `main`, đảm bảo mọi dòng code mới đều được tự động kiểm thử và kiểm tra cú pháp trước khi cho phép đóng gói.
- **Đóng góp về tính sẵn sàng và bảo mật:** Đảm bảo hệ thống vận hành ổn định nhờ cơ chế `healthcheck` và quản lý biến môi trường an toàn theo tiêu chuẩn 12-Factor App.
- **Ý thức làm việc nhóm:** Phối hợp chặt chẽ với các thành viên phụ trách Backend, Frontend và QA để tích hợp các tham số cổng, đường dẫn API và kịch bản test vào pipeline một cách đồng bộ, đúng tiến độ của Mini Project Session 13.
