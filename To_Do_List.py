class Task:
	def __init__(self,desc) -> None:
		self.desc=desc
		self.done=False
	
	def Mark_done(self):
		self.done=True
	
	def __str__(self):
		status="[X] " if self.done else "[ ] "
		return f"{status} | {self.desc}"
		
		
class Task_manager:
	def __init__(self) -> None:
		self.tasks=[]
	
	def Add_task(self) -> None:
		desc=input("Enter task descreption: ")
		new_task=Task(desc)
		self.tasks.append(new_task)
		print(f"Task Added: {desc}")
	
	def Show_task(self):
		if not self.tasks:
			print("No Task yet")
			return
		for index,task in enumerate(self.tasks):
			print(f"{index +1} | {task}")

	def Complete_task(self) -> None:
		task_num=int(input("Enter Task_num: "))
		index=task_num - 1
		if 0<=index<len(self.tasks):
			self.tasks[index].Mark_done()
			print("Task completed")
		else:
			print("The task doesn't exists")
	
	
	def  Delete_task(self) -> None:
			task_num=int(input("Enter Task_num: "))
			index=task_num-1
			if 0<=index<len(self.tasks):
				removed= self.tasks.pop(index)
				print(f"Deleted : {removed.desc}")
			else:
				print("Task doesn't exists")
	
	
			
	def Save_file(self,filename="file.txt"):
			with open(filename,"w") as f:
				for task in self.tasks:
					done="1" if task.done else "0"
					f.write(f"{done} | {task.desc} \n")
					
	
	def load_file(self,filename="file.txt"):
			try:
				with open(filename,"r") as f:
					for line in f:
						if "|" not in line:
							continue
						done,desc=line.strip().split("|",1)
						task=Task(desc)
						if done=="1":
							task.Mark_done()
						self.tasks.append(task)
			except FileNotFoundError:
						pass
						
					
				
				
			
		
	
def main():
	manager=Task_manager()
	manager.load_file()
	
	
	while True:
		print("\n===== TO-DO LIST =====\n")

		print("1. Show tasks")

		print("2. Add task")

		print("3. Complete task")

		print("4. Delete task")

		print("5. Quit \n")

		choice = input("Choose an option (1-5): ")
		
		if choice=="1":
			manager.Show_task()
		elif choice=="2":
			manager.Add_task()
		elif choice=="3":
			manager.Complete_task()
		elif choice=="4":
			manager.Delete_task()
		elif choice=="5":
			manager.Save_file()
			print("Good bye..")
			
			break
		else:
			print("invalid command..")
	
		
main()