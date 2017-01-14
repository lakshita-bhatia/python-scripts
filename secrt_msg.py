import os
def rename_file():
	file_list=os.listdir(r"")
	print(file_list)
	saved_path = os.getcwd()
	os.chdir(r"C:\OOP\prank")
	for file_name in file_list:
		os.rename(file_name,file_name.translate(none,"0123456789"))
	os.chdir(saved_path)
rename_files()
