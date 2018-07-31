from django.db import models
from django.views.generic.list import ListView
from django.contrib.auth.models import User
# Create your models here.
class Lac(models.Model):
	name=models.CharField(max_length=100)
	job_position=models.CharField(max_length=100)
	department=models.CharField(max_length=100)
	campus=models.CharField(max_length=100)
	type=models.CharField(max_length=100)
	ict_id=models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return "name : {}, job_position : {}, department : {}, campus : {}, type : {}, ict_id : {}".format(self.name,self.job_position,self.department,self.campus,self.type,self.ict_id)
	class Meta:
		ordering = ['id']

class Subject(models.Model):
	ExamT = (
		('0','Choice'),
		('1','Short answer'),
		('2','Short answer and Choice'),
		('3','Interview and Practice')
		)
	InstrucT = (
		('0','One Instructor'),
		('1','Multiple Instructor')
		)
	DegreeT = (
		('0','Bachelor'),
		('1','Master'),
		('2','Doctor')
		)
	examiner=models.CharField(max_length = 100,null = False,default = 'foo')
	Sid=models.CharField(max_length=5,default = 'foo')
	student=models.IntegerField(default='0')
	ratio=models.FloatField(default='0.0000')
	T_type=models.CharField(choices=ExamT,max_length = 1,default = 'Choice')
	S_type=models.CharField(choices=InstrucT,max_length = 1,default = '0')
	Degree=models.CharField(choices=DegreeT,max_length = 1,default = '0')
	yeasr=models.CharField(max_length = 6,null = False,default = '1/25xx')
	amount=models.IntegerField(null = False,default = 1)
	
	def __str__(self):
		return "examiner : {}, Sid : {}, student : {},ratio : {},T_type : {},S_type : {},Degree : {},yeasr : {}".format(self.examiner,self.ratio,self.student,self.Sid,self.T_type,self.S_type,self.Degree,self.yeasr)
	class Meta:
		ordering = ['examiner']


	
