from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os 
import platform
# Create your views here.
def home(request):
	return render(request ,"window/home.html")

def show_processes(request):
	your_sys = platform.system()
	taskhtml = '''<table style="width:100%"> <tr> <th> p-name </th> <th> p-id </th> </tr><br>'''
	tasks = subprocess.run('tasklist',shell=True, stdout=subprocess.PIPE )
	show = tasks.stdout.decode('utf-8').split('\n')
	for i in show[5:] : 
		new_str="<tr>" 
		a = i.find(".exe")
		a_name = i[0:int(a)+4]
		new_str += "<th>" + str(a_name) +"</th>"
		b_find = i[int(len(a_name)):]
		pr_id=""
		for kl in b_find :
			if kl.isdigit() :
				pr_id += kl
			elif kl.isalpha():break 
			else:pass
		new_str += "<th>" + str(pr_id) +"</th>"
		taskhtml += f"{new_str}"
	taskhtml += "</table>"
	html = "<html> <head> </head> <body> <table>" + taskhtml + " </table> </body> </html>"
	return HttpResponse(html)