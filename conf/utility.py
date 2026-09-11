from conf.config import FILE_NAME
import os
import csv


def get_data() -> list:
    data = []
    file_exists = os.path.exists(FILE_NAME)

    if not file_exists:
        return data

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def set_data(emp_id, name, email, mobile_number, role):

    file_exist = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # new file with header
        if not file_exist or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(["emp_id", "name", "email", "mobile_number", "role"])

        result = writer.writerow([emp_id, name, email, mobile_number, role])
        print(result)

    return


# def update_data(emp_id, name, email, mobile_number, role):

#     existing_data = get_data()

#     with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)

#         writer.writerow(["emp_id", "name", "email", "mobile_number", "role"])

#         for data in existing_data:
#             print(data)
#             if data["emp_id"] == emp_id:
#                 writer.writerow(
#                     [
#                         emp_id,
#                         name,
#                         email,
#                         mobile_number,
#                         role,
#                     ]
#                 )
#             else:
#                 writer.writerow(
#                     [
#                         data["emp_id"],
#                         data["name"],
#                         data["email"],
#                         data["mobile_number"],
#                         data["role"],
#                     ]
#                 )

#     return
