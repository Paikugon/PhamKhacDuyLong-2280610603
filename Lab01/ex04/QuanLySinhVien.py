from SinhVien import Student

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))
        sv = Student(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            sv._name = input("Nhập tên sinh viên: ")
            sv._gender = input("Nhập giới tính sinh viên: ")
            sv._major = input("Nhập chuyên ngành của sinh viên: ")
            sv._avgGrade = float(input("Nhập điểm của sinh viên: "))
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh viên có ID = {ID} không tồn tại")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        return [sv for sv in self.listSinhVien if keyword.upper() in sv._name.upper()]

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv):
        if sv._avgGrade >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._avgGrade >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._avgGrade >= 5:
            sv._hocLuc = "Trung bình"
        else:
            sv._avgGrade = "Yếu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Gender", "Major", "Diem TB", "Hoc Luc"))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._gender, sv._major, sv._avgGrade, sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
