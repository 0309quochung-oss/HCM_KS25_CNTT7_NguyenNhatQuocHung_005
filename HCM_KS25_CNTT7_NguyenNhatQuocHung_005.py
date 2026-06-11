jod_list = []

def check_index(working_day, completion_date):
    return working_day - completion_date


def check_progress(progress_index):
    if progress_index < 0:
        return "Hoàn thành sớm"
    elif progress_index == 0:
        return "Bình thường"
    elif progress_index > 3:
        return "Quá hạn"
    else:
        return "Cần tăng tốc"
    
def empty_input_check(thong_bao):
    while True:
        du_lieu = input(thong_bao)

        if du_lieu == "":
            print("Không được để trống")
            continue
            
        return du_lieu


def check_the_list():
    if len(jod_list) == 0:
        print("Danh sách đang trống")
        return False
    return True


def check_for_duplicates(id):
    for jod in jod_list:
        if jod["id"] == id:
            return jod
    return None


def larger_test(thong_bao):
    while True:
        try:
            gia_tri = int(input(thong_bao))
        
            if gia_tri <= 0:
                print("Phải là số nguyên lớn hơn 0")
                continue
            return gia_tri
        except:
            print("Vui lòng nhập số")
            continue


def add_list():
    while True:
        id = empty_input_check("Nhập mã công việc: ")
        if check_for_duplicates(id):
            print("Đã tồn tài mã này")
            continue
        break

    while True:
        job_title = empty_input_check("Nhập tên công việc: ")
        employee_name = empty_input_check("Nhập tên nhân viên: ")
        working_day = larger_test("Nhập số ngày dự kiến hoàn thành: ")
        completion_date = larger_test("Nhập số ngày thực tế: ")


        progress_index = check_index(working_day, completion_date)
        trang_thai = check_progress(progress_index)

        job_new = {
            "id": id,
            "job_title": job_title,
            "employee_name": employee_name,
            "working_day": working_day,
            "completion_date": completion_date,
            "progress_index": progress_index,
            "trang_thai": trang_thai
        }

        jod_list.append(job_new)
        print("Đã thêm công việc mới thành công")



def input_list():

    if not check_the_list():
        return
    
    print("="*110);

    print(
        f"| {"Mã công việc":<10}"
        f"| {"công việc/nhiệm vụ":<20}"
        f"| {"nhân viên thực hiện":<22}"
        f"| {"ngày dự kiến":<10}"
        f"| {"ngày thực tế":<10}"
        f"| {"chỉ số":<8}"
        f"| {"tiến độ":<10}"
    )

    print("="*110);

    for jod in jod_list:
        print(
            f"| {jod["id"]:<10}"
            f"| {jod["job_title"]:<20}"
            f"| {jod["employee_name"]:<22}"
            f"| {jod["working_day"]:<10}"
            f"| {jod["completion_date"]:<10}"
            f"| {jod["progress_index"]:<8}"
            f"| {jod["trang_thai"]:<10}"
        )
    
    print("="*110);


def update_list():
    if check_the_list():
        return
    while True:
        tim_ma = empty_input_check("Nhập mã cần tìm: ")
        if check_for_duplicates(tim_ma):
            while True:
                employee_name_new = empty_input_check("Nhập tên nhân viên: ")
                working_day_new = larger_test("Nhập số ngày dự kiến hoàn thành: ")
                completion_date_new = larger_test("Nhập số ngày thực tế: ")


                progress_index_new = check_index(working_day_new, completion_date_new)
                
                trang_thai_new = check_progress(progress_index_new)

                for jod in jod_list:
                    jod["employee_name"] = employee_name_new
                    jod[" working_day"] = working_day_new
                    jod["completion_date"] = completion_date_new
                    jod["progress_index"] = progress_index_new
                    jod["trang_thai"] = trang_thai_new

                print("cập nhật thành công");

        if tim_ma == None:
            print("Không tìm thấy mã")
            continue


def delete_list():
    if not check_the_list():
        return
    while True:
        tim_ma = empty_input_check("Nhập mã cần tìm: ")
        if check_for_duplicates(tim_ma):
            yeu_cau = input("Bạn có chắc là muốn xóa (Y/N): ").upper()

            for jod in jod_list: 
                if yeu_cau == "Y":
                    jod_list.remove(jod)
                    print("Đã xóa thành công")
                    break;
                else:
                    print("Đã hủy yêu cầu")
                    break;



def search_list():
    pass
def statistical_list():
    pass

def classify_list():
    pass
while True:
    menu_title = f"QUẢN LÝ DANH SÁCH CÔNG VIỆC".center(50,"=")
    choice = input(f"""
{menu_title}
1. Hiện thị danh sách công việc
2. Thêm công việc mới
3. cập nhật tiến độ thực tế
4. xóa công việc khỏi dự án
5. tìm kiếm công việc
6. thông kê trạng thái tiến độ
7. phân loại tiến dộ tự động
8. thoát chương trình
{"="*len(menu_title)}
nhập lựa chọn (1 - 8): """)
    
    match choice:
        case "1":
            input_list()
        case "2":
            add_list();
        case "3":
            update_list();
        case "4":
            delete_list();
        case "5":
            search_list();
        case "6":
            statistical_list();
        case "7":
            classify_list();
        case "8":
            print("Thoát chương trình thành công");
            break
        case _:
            print("Lỗi vui lòng nhập lại")