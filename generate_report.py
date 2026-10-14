import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_report():
    doc = docx.Document()

    # Thiết lập lề trang chuẩn văn bản học thuật (Top, Bottom, Left, Right: 1 inch = 2.54 cm)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Cấu hình Style mặc định
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    # ==================== TRANG BÌA ====================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_inst.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\nHỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG / RIKKEI ACADEMY\n")
    r1.bold = True
    r1.font.size = Pt(13)
    r2 = p_inst.add_run("KHOA CÔNG NGHỆ THÔNG TIN\n---------------------------------")
    r2.bold = True
    r2.font.size = Pt(12)

    doc.add_paragraph("\n\n")

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_title.add_run("BÁO CÁO MINI PROJECT TỔNG HỢP (SESSION 13)\nHỌC PHẦN: DEVOPS (IT209)\n\n")
    r_sub.font.size = Pt(14)
    r_sub.bold = True
    r_sub.font.color.rgb = RGBColor(0x1B, 0x5E, 0x20)

    r_main = p_title.add_run("ĐỀ TÀI:\nNÂNG CẤP VÀ TỰ ĐỘNG HÓA TRIỂN KHAI NỀN TẢNG CAMPUS HUB\nHỆ THỐNG KẾT NỐI VÀ TÌM NHÓM HỌC TẬP CHO SINH VIÊN\n")
    r_main.font.size = Pt(18)
    r_main.bold = True
    r_main.font.color.rgb = RGBColor(0x0D, 0x47, 0xA1)

    doc.add_paragraph("\n\n")

    p_info = doc.add_paragraph()
    p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_info.paragraph_format.line_spacing = 1.3
    p_info.add_run("Giảng viên hướng dẫn: ").bold = True
    p_info.add_run("ThS. Đinh Thành Nam\n")
    p_info.add_run("Nhóm sinh viên thực hiện: ").bold = True
    p_info.add_run("Nhóm DevOps Session 13\n")
    p_info.add_run("Danh sách thành viên (10 thành viên):\n").bold = True
    p_info.add_run("1. Phạm Hương Quỳnh (Trưởng nhóm)\n")
    p_info.add_run("2. Trần Thị Thu Trang\n")
    p_info.add_run("3. Phạm Minh Tuấn\n")
    p_info.add_run("4. Tô Anh Tuấn\n")
    p_info.add_run("5. Đỗ Tiến Đạt\n")
    p_info.add_run("6. Ngô Trung Chiến\n")
    p_info.add_run("7. Đặng Thanh Bình\n")
    p_info.add_run("8. Vũ Đức Huy Hoàng\n")
    p_info.add_run("9. Đỗ Đức Mạnh\n")
    p_info.add_run("10. Cao Chí Thiện\n")

    doc.add_paragraph("\n")
    p_date = doc.add_paragraph()
    p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_date = p_date.add_run("Hà Nội, Tháng 10 Năm 2026")
    r_date.font.italic = True

    doc.add_page_break()

    # Helper function định dạng Heading
    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(16)
        h.paragraph_format.space_after = Pt(6)
        run = h.add_run(text)
        run.bold = True
        run.font.size = Pt(15)
        run.font.color.rgb = RGBColor(0x0D, 0x47, 0xA1)
        return h

    def add_h2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(4)
        run = h.add_run(text)
        run.bold = True
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(0x1B, 0x5E, 0x20)
        return h

    def add_screenshot_placeholder(caption):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(8)
        run_box = p.add_run(f"[HÌNH ẢNH MINH HỌA: {caption}]\n(Dán ảnh chụp màn hình thực tế tại vị trí này)")
        run_box.bold = True
        run_box.font.color.rgb = RGBColor(0x75, 0x75, 0x75)
        run_box.font.size = Pt(11)

    # ==================== PHẦN 1 ====================
    add_h1("1. TÓM TẮT SẢN PHẨM VÀ THÔNG TIN TRUY CẬP")
    p = doc.add_paragraph()
    p.add_run("Campus Hub là nền tảng chia sẻ thông tin trực tuyến trong khuôn viên trường đại học, kết nối sinh viên nhằm chia sẻ sự kiện, tìm đồ thất lạc, trao đổi học tập và giải quyết vấn đề thiết thực nhất của sinh viên: ")
    p.add_run("tìm kiếm bạn cùng nhóm để làm bài tập lớn, đồ án và tham gia các hoạt động ngoại khóa.").bold = True
    p.add_run("\n\nDự án được phát triển dựa trên dự án nền ")
    p.add_run("Campus Hub Base (React + Spring Boot + MySQL)").italic = True
    p.add_run(", được nhóm nâng cấp thêm chức năng nghiệp vụ ")
    p.add_run("Tuyển thành viên & Quản lý đơn ứng tuyển nhóm").bold = True
    p.add_run(", đồng thời hiện đại hóa toàn bộ hạ tầng bằng Docker, Docker Compose và tích hợp quy trình CI/CD tự động bằng GitHub Actions.")

    add_h2("1.1. Thông tin truy cập và triển khai hệ thống")
    table_info = doc.add_table(rows=6, cols=2)
    table_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_info.style = 'Table Grid'
    
    info_data = [
        ("Tên sản phẩm", "Campus Hub - Hệ thống kết nối & Tuyển nhóm học tập sinh viên"),
        ("Liên kết GitHub", "https://github.com/dinhthanhnam/campus-hub-base (Nhánh main)"),
        ("Phiên bản / Commit ID bảo vệ", "Commit mới nhất trên nhánh main (đã gắn tag v1.1-final)"),
        ("Đường dẫn triển khai công khai", "https://campus-hub-devops.onrender.com (hoặc IP VPS nhóm cung cấp)"),
        ("Tài khoản Sinh viên demo", "Username: student  |  Mật khẩu: student123"),
        ("Tài khoản Quản trị viên demo", "Username: admin    |  Mật khẩu: admin123")
    ]
    for i, (k, v) in enumerate(info_data):
        row = table_info.rows[i]
        c1, c2 = row.cells[0], row.cells[1]
        c1.text = k
        c1.paragraphs[0].runs[0].bold = True
        set_cell_background(c1, "F0F4F8")
        c2.text = v
        set_cell_margins(c1)
        set_cell_margins(c2)

    add_h2("1.2. Bảng phân công công việc và đánh giá đóng góp của 10 thành viên")
    doc.add_paragraph("Để đảm bảo dự án hoàn thành đúng tiến độ và đáp ứng toàn diện các tiêu chí của Mini Project DevOps Session 13, khối lượng công việc được phân bổ đồng đều cho cả 10 thành viên theo đúng chuyên môn và vai trò:")

    members_task_data = [
        ("1", "Phạm Hương Quỳnh", "Trưởng nhóm / Project Manager & Architect", "Quản lý tiến độ dự án; phân tích bài toán & thiết kế kiến trúc hệ thống; điều phối buổi bảo vệ & tổng duyệt báo cáo.", "100%"),
        ("2", "Trần Thị Thu Trang", "Business Analyst & UI/UX Designer", "Đặc tả luồng nghiệp vụ (User Flow); thiết kế Wireframe giao diện (tiến độ tuyển nhóm, modal ứng tuyển, quản lý ứng viên); viết phần 2, 3 báo cáo.", "100%"),
        ("3", "Phạm Minh Tuấn", "Database Engineer & Backend Core", "Thiết kế mô hình CSDL (ERD); xây dựng Flyway migration V2__add_group_membership.sql; tạo Entity GroupMembership, Enum, Repository.", "100%"),
        ("4", "Tô Anh Tuấn", "Backend API & Security Developer", "Lập trình logic xử lý tuyển nhóm trong PostService (duyệt đơn, tự động chốt nhóm RESOLVED); xây dựng 4 REST API trong PostController; bảo mật Spring Security.", "100%"),
        ("5", "Đỗ Tiến Đạt", "Frontend Developer (Component & State)", "Phát triển component React: PostCard (hiển thị badge), PostDetail (thanh tiến độ tuyển trực quan); form tạo bài có targetMembers; xử lý validation.", "100%"),
        ("6", "Ngô Trung Chiến", "Frontend Developer (API & Dashboard)", "Tích hợp API ứng tuyển trong App.jsx và api.js; xây dựng bảng điều khiển quản lý ứng viên cho chủ bài; thiết kế CSS Responsive (styles.css).", "100%"),
        ("7", "Đặng Thanh Bình", "QA & Automated Testing Engineer", "Viết bộ kiểm thử tích hợp PostApiIntegrationTest.java (MockMvc, các kịch bản thành công và ngoại lệ); kiểm tra chuẩn mã nguồn ESLint; lập tài liệu test.", "100%"),
        ("8", "Vũ Đức Huy Hoàng", "DevOps Engineer (Containerization)", "Xây dựng Dockerfile Multi-stage cho Backend (JRE 21 Temurin, user non-root spring); xây dựng Dockerfile Frontend; cấu hình Nginx Reverse Proxy (nginx.conf).", "100%"),
        ("9", "Đỗ Đức Mạnh", "DevOps Engineer (Orchestration & CI/CD)", "Viết docker-compose.yml điều phối 3 services (MySQL 8.4, Backend, Frontend, healthcheck, volume); thiết lập GitHub Actions CI/CD (.github/workflows/ci.yml); quản lý .env.", "100%"),
        ("10", "Cao Chí Thiện", "Release Engineer & Presentation Lead", "Triển khai hệ thống lên môi trường công khai (Render/VPS, HTTPS, Actuator healthcheck); thu thập ảnh chụp minh chứng kiểm thử; chuẩn bị slide và kịch bản demo bảo vệ.", "100%")
    ]

    table_members = doc.add_table(rows=11, cols=5)
    table_members.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_members.style = 'Table Grid'
    member_headers = ["STT", "Họ và tên", "Vai trò", "Nhiệm vụ cụ thể phụ trách", "Đánh giá"]
    for j, h in enumerate(member_headers):
        c = table_members.rows[0].cells[j]
        c.text = h
        c.paragraphs[0].runs[0].bold = True
        set_cell_background(c, "D9E2EC")
        set_cell_margins(c)

    for i, row_data in enumerate(members_task_data):
        row = table_members.rows[i+1]
        for j, val in enumerate(row_data):
            c = row.cells[j]
            c.text = val
            set_cell_margins(c)
            if j == 0 or j == 4:
                c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            elif j == 1:
                c.paragraphs[0].runs[0].bold = True

    # ==================== PHẦN 2 ====================
    add_h1("2. PHÂN TÍCH BÀI TOÁN, NGƯỜI DÙNG VÀ PHẠM VI")
    add_h2("2.1. Bối cảnh và Vấn đề cần giải quyết")
    doc.add_paragraph(
        "Trong hầu hết các môn học chuyên ngành công nghệ thông tin (như DevOps, Công nghệ phần mềm, Hệ quản trị CSDL), "
        "sinh viên bắt buộc phải làm bài tập lớn hoặc mini project theo nhóm từ 2 đến 4 người. Tuy nhiên, việc ghép nhóm hiện nay gặp nhiều rào cản:\n"
        "• Sinh viên thường đăng bài tìm nhóm trên các hội nhóm Facebook hoặc nhóm chat Zalo chung của lớp, dẫn đến tình trạng bài đăng bị trôi rất nhanh.\n"
        "• Người muốn xin gia nhập không biết nhóm đã đủ người hay chưa, dẫn đến mất thời gian nhắn tin hỏi trùng lặp.\n"
        "• Trưởng nhóm khó quản lý thông tin liên hệ và lý do xin tham gia của từng ứng viên một cách tập trung, minh bạch."
    )

    add_h2("2.2. Đối tượng sử dụng")
    doc.add_paragraph(
        "• Sinh viên (USER): Đăng tin tuyển bạn cùng nhóm (chỉ rõ số lượng cần tìm), tìm kiếm các bài tuyển nhóm phù hợp, "
        "gửi đơn xin tham gia kèm lời nhắn và số điện thoại/Zalo; nếu là chủ nhóm có quyền duyệt hoặc từ chối ứng viên.\n"
        "• Quản trị viên (ADMIN): Giám sát toàn bộ nội dung bài đăng, có quyền ẩn các bài vi phạm hoặc hỗ trợ quản lý trạng thái hệ thống."
    )

    add_h2("2.3. Giá trị phiên bản của nhóm mang lại")
    doc.add_paragraph(
        "Phiên bản nâng cấp mang lại giá trị thực tiễn vượt trội so với bản mẫu bằng cách số hóa trọn vẹn luồng tìm nhóm:\n"
        "1. Trực quan hóa tiến độ tuyển: Hiển thị thanh tiến độ số thành viên đã tuyển trên chỉ tiêu (ví dụ: 2/3 thành viên).\n"
        "2. Đăng ký & Xét duyệt 2 chiều: Sinh viên gửi đơn kèm lời nhắn và thông tin liên hệ; chủ nhóm có bảng điều khiển để duyệt (Chấp nhận / Từ chối).\n"
        "3. Tự động hóa trạng thái: Khi duyệt đủ số lượng thành viên mục tiêu, hệ thống tự động đánh dấu bài viết hoàn tất (RESOLVED) và đóng tiếp nhận đơn mới, chống quá tải."
    )

    add_h2("2.4. Quản lý phạm vi dự án (In-Scope và Out-of-Scope)")
    doc.add_paragraph(
        "Tuân thủ nghiêm ngặt chỉ đạo của giảng viên: 'Một phạm vi nhỏ, hoàn chỉnh và có lý do rõ ràng phù hợp hơn một hệ thống lớn nhưng thiếu nhất quán', nhóm đã phân định rõ phạm vi:\n"
        "• Các chức năng thực hiện (In-Scope):\n"
        "  - Bổ sung trường số lượng thành viên mục tiêu khi đăng bài tuyển nhóm.\n"
        "  - Sinh viên nộp đơn ứng tuyển kèm thông tin liên hệ và lời nhắn giới thiệu.\n"
        "  - Chủ nhóm xem danh sách ứng viên, thực hiện phê duyệt hoặc từ chối.\n"
        "  - Tự động đóng tuyển khi đủ chỉ tiêu; hỗ trợ sinh viên hủy đơn khi chưa duyệt.\n"
        "  - Đóng gói container hóa 100% bằng Docker và thiết lập CI/CD tự động bằng GitHub Actions.\n"
        "• Các nội dung chủ động KHÔNG thực hiện (Out-of-Scope) & Lý do:\n"
        "  - Không tích hợp Chat realtime / WebSocket phức tạp: Nhằm tránh làm phình to kiến trúc hệ thống, tránh lỗi đồng bộ dữ liệu phân tán; sinh viên đã có thông tin liên hệ (SĐT/Zalo) để trao đổi trực tiếp sau khi được duyệt.\n"
        "  - Không tích hợp cổng thanh toán trực tuyến: Vì đây là nền tảng học tập sinh viên phi thương mại.\n"
        "  - Không lưu trữ tệp tin video nặng: Tập trung tối ưu hóa tài nguyên máy chủ và tốc độ phản hồi API."
    )

    add_h2("2.5. Điểm khác biệt chính so với dự án nền")
    table_diff = doc.add_table(rows=4, cols=3)
    table_diff.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_diff.style = 'Table Grid'
    headers = ["Tiêu chí so sánh", "Campus Hub Base (Dự án nền)", "Phiên bản Nhóm nâng cấp"]
    for j, h in enumerate(headers):
        cell = table_diff.rows[0].cells[j]
        cell.text = h
        cell.paragraphs[0].runs[0].bold = True
        set_cell_background(cell, "D9E2EC")
        set_cell_margins(cell)

    diff_rows = [
        ("Nghiệp vụ Tìm nhóm", "Chỉ có chuyên mục 'Tìm nhóm' dạng bài viết tĩnh, người dùng phải bình luận tự do để trao đổi.", "Chức năng tuyển nhóm chuyên dụng: Cho phép đặt chỉ tiêu, nộp đơn ứng tuyển, lưu thông tin liên lạc và phê duyệt trạng thái khép kín."),
        ("Đóng gói & Vận hành", "Chưa có Docker. Chạy thủ công trên máy bằng gradle và npm, dễ phát sinh lỗi môi trường (Java version, port, dependency).", "Đóng gói toàn diện bằng Dockerfile Multi-stage (Backend JRE 21, Frontend Nginx) và docker-compose.yml 1 lệnh khởi chạy 3 service."),
        ("Quy trình CI/CD", "Chưa có pipeline tự động. Phải kiểm thử thủ công từng thành phần.", "Tích hợp GitHub Actions tự động kiểm thử Unit/Integration test, kiểm tra chuẩn mã nguồn (ESLint) và build Docker image mỗi khi push.")
    ]
    for i, row in enumerate(diff_rows):
        for j in range(3):
            cell = table_diff.rows[i+1].cells[j]
            cell.text = row[j]
            set_cell_margins(cell)

    # ==================== PHẦN 3 ====================
    add_h1("3. LUỒNG SỬ DỤNG VÀ THIẾT KẾ GIAO DIỆN")
    add_h2("3.1. Kịch bản luồng sử dụng chính (User Flow)")
    doc.add_paragraph(
        "Luồng tuyển nhóm và đăng ký tham gia diễn ra qua 4 giai đoạn mạch lạc:\n"
        "• Bước 1 (Tạo bài tuyển): Sinh viên đăng nhập, bấm 'Đăng bài', chọn chuyên mục 'Tìm nhóm' và nhập số lượng thành viên cần tìm (ví dụ: 3 người).\n"
        "• Bước 2 (Ứng tuyển): Sinh viên khác thấy bài viết, bấm xem chi tiết -> Thấy thanh tiến độ chưa đầy -> Bấm 'Đăng ký tham gia nhóm' -> Nhập lời nhắn giới thiệu bản thân và thông tin liên hệ (SĐT/Zalo) -> Gửi yêu cầu.\n"
        "• Bước 3 (Duyệt đơn): Chủ bài viết vào chi tiết bài của mình -> Hệ thống hiển thị bảng 'Danh sách ứng viên đăng ký tham gia' -> Chủ bài xem xét thông tin và bấm 'Chấp nhận' hoặc 'Từ chối'.\n"
        "• Bước 4 (Tự động chốt nhóm): Khi số lượng ứng viên được chấp nhận đạt đủ chỉ tiêu, bài viết tự động chuyển trạng thái thành RESOLVED (Hoàn tất), hiển thị thông báo 'Đã đủ thành viên'."
    )

    add_h2("3.2. Xử lý các trường hợp ngoại lệ và dữ liệu không hợp lệ")
    doc.add_paragraph(
        "Hệ thống thiết kế các chốt chặn kiểm tra chặt chẽ ở cả Frontend và Backend API:\n"
        "• Tự ứng tuyển vào bài của chính mình: Hệ thống báo lỗi 400 Bad Request ('Bạn là chủ bài đăng, không thể tự ứng tuyển').\n"
        "• Ứng tuyển trùng lặp: Nếu đã có đơn PENDING hoặc ACCEPTED, nút đăng ký bị ẩn và hệ thống báo lỗi nếu cố ý gọi API.\n"
        "• Ứng tuyển khi nhóm đã đủ hoặc bài đã đóng: Không cho phép gửi đơn vào bài viết có trạng thái khác PUBLISHED hoặc khi số người được duyệt đã đạt chỉ tiêu.\n"
        "• Kiểm tra quyền hạn duyệt: Chỉ có tác giả bài viết hoặc tài khoản ADMIN mới có quyền duyệt đơn của ứng viên."
    )

    add_h2("3.3. Minh họa giao diện thực tế của hệ thống")
    add_screenshot_placeholder("Giao diện Trang chủ hiển thị bài đăng có huy hiệu 'Tuyển nhóm: x/y người'")
    add_screenshot_placeholder("Giao diện Chi tiết bài viết với Thanh tiến độ tuyển nhóm và Hộp thoại Ứng tuyển")
    add_screenshot_placeholder("Bảng điều khiển Quản lý danh sách ứng viên (Dành riêng cho chủ bài viết)")

    # ==================== PHẦN 4 ====================
    add_h1("4. THIẾT KẾ CHỨC NĂNG, API VÀ DỮ LIỆU")
    add_h2("4.1. Danh sách API mở rộng")
    table_api = doc.add_table(rows=5, cols=4)
    table_api.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_api.style = 'Table Grid'
    api_headers = ["Phương thức", "Endpoint URL", "Chức năng nghiệp vụ", "Xác thực"]
    for j, h in enumerate(api_headers):
        c = table_api.rows[0].cells[j]
        c.text = h
        c.paragraphs[0].runs[0].bold = True
        set_cell_background(c, "D9E2EC")
        set_cell_margins(c)

    api_data = [
        ("POST", "/api/posts/{id}/memberships", "Gửi đơn đăng ký tham gia nhóm (kèm message & contactInfo)", "Có (HTTP Basic)"),
        ("DELETE", "/api/posts/{id}/memberships/me", "Sinh viên tự hủy đơn đăng ký đang chờ duyệt của mình", "Có (HTTP Basic)"),
        ("PATCH", "/api/posts/{id}/memberships/{mId}/status", "Chủ nhóm cập nhật trạng thái đơn (ACCEPTED / REJECTED)", "Có (Owner/Admin)"),
        ("GET", "/api/posts/{id}/memberships", "Lấy toàn bộ danh sách đơn ứng tuyển của bài viết", "Có (Owner/Admin)")
    ]
    for i, row in enumerate(api_data):
        for j in range(4):
            c = table_api.rows[i+1].cells[j]
            c.text = row[j]
            set_cell_margins(c)

    add_h2("4.2. Sơ đồ phối hợp giữa Frontend, Reverse Proxy, Backend và Database")
    doc.add_paragraph(
        "Trình tự tương tác khi người dùng gửi đơn ứng tuyển:\n"
        "1. Người dùng thao tác trên React Frontend -> Gửi HTTP POST request tới '/api/posts/{id}/memberships'.\n"
        "2. Nginx Container lắng nghe tại Port 80, nhận diện tiền tố '/api/' -> Thực hiện Reverse Proxy chuyển tiếp nội bộ sang Backend Container (Port 8080).\n"
        "3. Spring Boot tiếp nhận request -> SecurityFilter kiểm tra HTTP Basic Auth -> Chuyển vào PostController.\n"
        "4. PostService kiểm tra các quy tắc nghiệp vụ: xác định bài đăng có tồn tại không, kiểm tra user có phải chủ bài không, kiểm tra đã nộp đơn chưa.\n"
        "5. GroupMembershipRepository thực thi câu lệnh SQL INSERT lưu bản ghi vào MySQL Container qua kết nối JDBC.\n"
        "6. Kết quả phản hồi HTTP 201 Created trả về cho Frontend cập nhật lại giao diện ngay lập tức."
    )

    add_h2("4.3. Thiết kế Cơ sở Dữ liệu & Flyway Migration")
    doc.add_paragraph(
        "Hệ thống quản lý phiên bản cơ sở dữ liệu bằng Flyway Migration. File V2__add_group_membership.sql đã được bổ sung:\n"
        "1. Bổ sung cột target_members vào bảng posts: Kiểu INT, lưu số lượng thành viên mục tiêu cần tìm.\n"
        "2. Tạo bảng mới group_memberships với các trường:\n"
        "   - id (BIGINT, Primary Key, Auto Increment)\n"
        "   - post_id (BIGINT, Foreign Key trỏ tới posts, ON DELETE CASCADE)\n"
        "   - user_id (BIGINT, Foreign Key trỏ tới users)\n"
        "   - message (VARCHAR(500), Lời nhắn khi ứng tuyển)\n"
        "   - contact_info (VARCHAR(100), SĐT hoặc Zalo để liên hệ)\n"
        "   - status (VARCHAR(20), Trạng thái đơn: PENDING, ACCEPTED, REJECTED)\n"
        "   - created_at, updated_at (DATETIME(6))\n"
        "   - Ràng buộc UNIQUE(post_id, user_id) đảm bảo mỗi sinh viên chỉ gửi tối đa 1 đơn cho một bài viết."
    )

    # ==================== PHẦN 5 ====================
    add_h1("5. KIẾN TRÚC PHẦN MỀM VÀ TRIỂN KHAI DEVOPS")
    add_h2("5.1. Kiến trúc Hệ thống Tổng thể")
    doc.add_paragraph(
        "Hệ thống được thiết kế theo mô hình Micro-service ready với 3 tầng độc lập được cô lập trong Docker Network:\n"
        "• Tầng Trình diễn (Frontend Container): Đóng gói ứng dụng React SPA bằng Web Server Nginx Alpine (Port 80). Nginx đóng vai trò là Reverse Proxy, phục vụ các file tĩnh cực nhanh và chuyển tiếp các request có tiền tố /api/ sang tầng Backend.\n"
        "• Tầng Xử lý Nghiệp vụ (Backend Container): Chạy Spring Boot monolith trên nền OpenJDK 21 (Port 8080). Tiếp nhận các yêu cầu RESTful API, thực thi xác thực bảo mật Spring Security và quản lý giao dịch dữ liệu.\n"
        "• Tầng Lưu trữ Dữ liệu (Database Container): Sử dụng MySQL 8.4 (Port 3306), kết nối nội bộ qua mạng Docker bridge, dữ liệu được gắn kết bền vững qua Docker Volume (mysql_data) tránh mất mát khi restart container."
    )

    add_h2("5.2. Kỹ thuật Containerization & Tối ưu hóa Docker")
    doc.add_paragraph(
        "Nhóm áp dụng triệt để kỹ thuật Multi-stage build nhằm giảm thiểu kích thước hình ảnh (image size) và gia tăng độ bảo mật:\n"
        "• Backend Dockerfile: Gồm 2 stage:\n"
        "   - Stage 1 (Build): Dùng base image eclipse-temurin:21-jdk để tải dependency và biên dịch file JAR.\n"
        "   - Stage 2 (Runtime): Chỉ copy file JAR đã build sang image eclipse-temurin:21-jre siêu nhẹ. Tạo người dùng phi đặc quyền (non-root user: spring) để chạy ứng dụng, ngăn chặn nguy cơ leo thang đặc quyền khi bị tấn công.\n"
        "• Frontend Dockerfile: Gồm 2 stage:\n"
        "   - Stage 1 (Build): Dùng node:20-alpine chạy npm ci và vite build.\n"
        "   - Stage 2 (Serve): Copy thư mục dist vào nginx:alpine (dung lượng image chỉ vỏn vẹn ~30MB).\n"
        "• docker-compose.yml: Điều phối 3 service, tích hợp cơ chế healthcheck để đảm bảo Backend chỉ khởi động sau khi MySQL đã sẵn sàng nhận kết nối."
    )

    add_h2("5.3. Quy trình CI/CD Pipeline (GitHub Actions)")
    doc.add_paragraph(
        "Quy trình Tích hợp và Triển khai liên tục (CI/CD) được cấu hình tự động tại .github/workflows/ci.yml, kích hoạt mỗi khi có commit hoặc Pull Request vào nhánh main:\n"
        "• Job 1 (Backend Tests): Chạy trên máy ảo Ubuntu, cài đặt JDK 21 Temurin, chạy toàn bộ bộ kiểm thử tự động (./gradlew test) và đóng gói bootJar.\n"
        "• Job 2 (Frontend Check): Cài đặt Node.js 20, kiểm tra lỗi cú pháp và quy chuẩn mã nguồn với ESLint (npm run lint), kiểm tra build tĩnh (npm run build).\n"
        "• Job 3 (Docker Build Verification): Sau khi 2 job trên thành công, tự động build thử nghiệm cả 2 Docker image để đảm bảo không xảy ra lỗi đóng gói khi triển khai thực tế."
    )

    add_h2("5.4. Quản lý Cấu hình và Bảo mật Secret")
    doc.add_paragraph(
        "Theo đúng chuẩn 12-Factor App và yêu cầu đề bài môn DevOps:\n"
        "• Không lưu mật khẩu, thông tin kết nối nhạy cảm trong mã nguồn công khai (GitHub repository).\n"
        "• File .env đã được cấu hình trong .gitignore.\n"
        "• Cung cấp file .env.example mẫu để người vận hành thiết lập biến môi trường khi triển khai trên máy chủ thật."
    )

    # ==================== PHẦN 6 ====================
    add_h1("6. NỘI DUNG ĐÃ PHÁT TRIỂN MỚI SO VỚI DỰ ÁN NỀN")
    doc.add_paragraph(
        "Tổng hợp những đóng góp và nâng cấp mà nhóm đã hoàn thành trên dự án nền Campus Hub:\n"
        "1. Cơ sở dữ liệu: Thiết kế bảng group_memberships, thêm cột target_members cho bảng posts, viết migration script V2__add_group_membership.sql.\n"
        "2. Backend Java: Tạo mới Entity GroupMembership, Enum MembershipStatus, Repository GroupMembershipRepository; mở rộng PostDtos, bổ sung 4 API endpoints mới trong PostController và logic xử lý giao dịch tự động chốt nhóm trong PostService.\n"
        "3. Kiểm thử tự động: Viết thêm kịch bản kiểm thử tích hợp (Integration Test) trong PostApiIntegrationTest kiểm tra toàn diện luồng tuyển nhóm, từ chối ứng tuyển chính chủ và duyệt ứng viên.\n"
        "4. Giao diện người dùng: Thiết kế huy hiệu tuyển nhóm trên PostCard, thanh tiến độ trực quan trên PostDetail, hộp thoại đăng ký tham gia ApplyDialog, bảng quản lý ứng viên cho chủ nhóm, và đồng bộ trạng thái thẻ tức thời.\n"
        "5. Hạ tầng DevOps: Thiết lập toàn bộ Dockerfile (Backend & Frontend), cấu hình Reverse Proxy Nginx, điều phối Docker Compose và thiết lập quy trình CI/CD GitHub Actions hoàn chỉnh."
    )

    # ==================== PHẦN 7 ====================
    add_h1("7. KẾT QUẢ KIỂM THỬ VÀ MINH CHỨNG VẬN HÀNH")
    add_h2("7.1. Kết quả Kiểm thử Backend (Unit & Integration Tests)")
    doc.add_paragraph(
        "Toàn bộ các ca kiểm thử tích hợp đã vượt qua thành công với kết quả BUILD SUCCESSFUL:\n"
        "• publicUserCanReadSeededPosts: Đọc thành công dữ liệu khởi tạo mẫu -> PASSED.\n"
        "• anonymousUserCannotCreatePost: Khách vãng lai không thể tạo bài (401 Unauthorized) -> PASSED.\n"
        "• authenticatedUserCanCreatePost: Sinh viên đăng nhập tạo bài thành công -> PASSED.\n"
        "• invalidPostReturnsReadableMessage: Báo lỗi khi thiếu dữ liệu tiêu đề/nội dung -> PASSED.\n"
        "• userCanApplyForGroupMembershipAndAuthorCanApprove: Kiểm tra luồng ứng tuyển, chặn chủ bài tự ứng tuyển, gửi đơn và duyệt đơn thành công -> PASSED.\n"
        "Thời gian thực thi: 20 giây. Trạng thái: 5 actionable tasks (100% passed)."
    )
    add_screenshot_placeholder("Ảnh chụp màn hình kết quả chạy './gradlew.bat test' đạt BUILD SUCCESSFUL")

    add_h2("7.2. Kết quả Kiểm thử Frontend (Linting & Build)")
    doc.add_paragraph(
        "• Lệnh 'npm run lint': Đạt chuẩn ESLint, 0 lỗi, 0 cảnh báo.\n"
        "• Lệnh 'npm run build': Vite biên dịch thành công 17 modules trong 156ms, tạo file tĩnh production tối ưu trong thư mục dist."
    )
    add_screenshot_placeholder("Ảnh chụp màn hình kết quả 'npm run lint' và 'npm run build' thành công")

    add_h2("7.3. Hướng dẫn Khởi chạy Hệ thống trên Máy chủ Thực tế")
    doc.add_paragraph(
        "Để chạy ứng dụng trên máy chủ (hoặc máy chấm thi của Giảng viên), chỉ cần thực hiện 2 lệnh:\n"
        "```powershell\n"
        "copy .env.example .env\n"
        "docker compose up --build -d\n"
        "```\n"
        "Sau khi lệnh hoàn tất, toàn bộ hệ sinh thái sẽ hoạt động tại http://localhost (Cổng 80).\n"
        "Kiểm tra tình trạng sức khỏe hệ thống: http://localhost:8080/actuator/health trả về {\"status\":\"UP\"}."
    )
    add_screenshot_placeholder("Ảnh chụp màn hình terminal chạy 'docker compose ps' hiển thị 3 container UP")

    # ==================== PHẦN 8 ====================
    add_h1("8. HẠN CHẾ HIỆN TẠI VÀ HƯỚNG PHÁT TRIỂN")
    doc.add_paragraph(
        "8.1. Hạn chế hiện tại:\n"
        "• Hệ thống hiện thông báo kết quả duyệt đơn qua giao diện khi sinh viên vào xem bài đăng, chưa có tính năng gửi email tự động hoặc thông báo đẩy thời gian thực (Push Notification).\n"
        "• Chưa có tính năng chat riêng trực tiếp giữa các thành viên sau khi được duyệt vào nhóm.\n\n"
        "8.2. Hướng phát triển trong tương lai:\n"
        "• Tích hợp WebSocket (Spring WebSocket + STOMP) để gửi thông báo realtime khi có ứng viên mới đăng ký hoặc khi đơn được duyệt.\n"
        "• Bổ sung dịch vụ gửi mail tự động (Spring Mail) thông báo thông tin liên lạc của các thành viên khi nhóm đã chốt đủ người.\n"
        "• Mở rộng cụm dịch vụ lên Kubernetes (K8s) với cơ chế Horizontal Pod Autoscaler (HPA) khi lượng người dùng tăng cao trong các đợt làm đồ án tập trung."
    )

    try:
        doc.save("BAO_CAO_MINI_PROJECT_SESSION13.docx")
        print("Successfully generated BAO_CAO_MINI_PROJECT_SESSION13.docx")
    except Exception as e:
        print("Could not save to primary filename:", e)

    try:
        doc.save("BAO_CAO_MINI_PROJECT_SESSION13_UPDATED.docx")
        print("Successfully generated BAO_CAO_MINI_PROJECT_SESSION13_UPDATED.docx")
    except Exception as e:
        print("Could not save to updated filename:", e)

if __name__ == '__main__':
    create_report()
