from fastapi import UploadFile, File
import zipfile
import io
from CodeAnalysis import CodeAnalysis
import matplotlib.pyplot as plt
import os
from pymongo import MongoClient
from db import collection, save_version


class Graph:
    def __init__(self, file: UploadFile):
        self.graph_image = []
        self.file = file

    def get_graph_image(self):
        error_dict = {
            "long_file": 0,
            "long_function": 0,
            "function_without_docstrings": 0,
            "unused_variable": 0
        }
        count_error_for_file = {}
        count_error = 0

        content = self.file.file.read()  # קריאה לתוכן הקובץ
        zip_bytes = io.BytesIO(content)

        with zipfile.ZipFile(zip_bytes) as z:
            for file_info in z.infolist():
                if file_info.filename.endswith('.py'):
                    with z.open(file_info) as f:
                        code_str = f.read().decode('utf-8')

                    self.__get_histogram(code_str, file_info.filename)
                    count_error_for_file[file_info.filename] = 0

                    if CodeAnalysis.number_of_lines(code_str) > 200:
                        error_dict["long_file"] += 1
                        count_error_for_file[file_info.filename] += 1
                        count_error += 1

                    func_len = CodeAnalysis.get_functions_lengths(code_str)
                    for key, value in func_len.items():
                        if value > 20:
                            error_dict["long_function"] += 1
                            count_error_for_file[file_info.filename] += 1
                            count_error += 1

                    count_without_docstring = len(CodeAnalysis.get_functions_without_docstrings(code_str))
                    error_dict["function_without_docstrings"] += count_without_docstring
                    count_error_for_file[file_info.filename] += count_without_docstring
                    count_error += count_without_docstring

                    count_unused_variable = len(CodeAnalysis.get_unused_variables(code_str))
                    error_dict["unused_variable"] += count_unused_variable
                    count_error_for_file[file_info.filename] += count_unused_variable
                    count_error += count_unused_variable

        save_version(count_error)
        self.create_pie_chart(error_dict)
        self.create_bar_chart(count_error_for_file)
        self.create_line_chart(self.get_versions_for_chart())
        return self.graph_image



    def __get_histogram(self, code_str: str, filename: str):
        func_lengths = CodeAnalysis.get_functions_lengths(code_str)
        lengths = list(func_lengths.values())
        names = list(func_lengths.keys())
        if not lengths:
            return

        plt.figure(figsize=(10, 6))
        plt.bar(names, lengths, color='pink', edgecolor='black')
        plt.title("Function Lengths")
        plt.xlabel("Function Name")
        plt.ylabel("Length (in lines)")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        output_path = os.path.join(
            os.getcwd(), "Graphs", f"{filename}_hist.png"
        )
        plt.savefig(output_path)
        plt.close()
        self.graph_image.append(output_path)

    def create_pie_chart(self, error_dict):
        labels = list(error_dict.keys())
        sizes = list(error_dict.values())
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Error Types Distribution")
        plt.axis('equal')
        output_path = os.path.join(
            os.getcwd(),"Graphs",
            "pie chart.png"
        )
        plt.savefig(output_path)
        plt.close()
        self.graph_image.append(output_path)

    def create_bar_chart(self, error_dict):
        files = list(error_dict.keys())
        problems = list(error_dict.values())
        plt.figure(figsize=(8, 5))
        plt.bar(files, problems, color='skyblue')
        plt.xlabel('File Name')
        plt.ylabel('Number of Problems')
        plt.title('Problems per File')
        plt.xticks(rotation=45)
        plt.tight_layout()
        output_path = os.path.join(
           os.getcwd(),"Graphs",
            "bar chart.png"
        )
        plt.savefig(output_path)
        plt.close()
        self.graph_image.append(output_path)

    def create_line_chart(self, data):
        dates = [item["date"] for item in data]
        issues = [item["issues"] for item in data]

        plt.figure(figsize=(10, 5))
        plt.plot(dates, issues, marker='o', color='blue')
        plt.xlabel("Date")
        plt.ylabel("Number of Issues")
        plt.title("Issues per Version Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        output_path = os.path.join(
            os.getcwd(),"Graphs",
            "line chart.png"
        )
        plt.savefig(output_path)
        plt.close()
        self.graph_image.append(output_path)

    def get_versions_for_chart(self):
        data = collection.find().sort("date", 1)  # שליפה לפי סדר כרונולוגי
        return [
            {
                "date": d["date"].strftime("%Y-%m-%d %H:%M"),
                "issues": d["issue_count"]
            }
            for d in data
        ]