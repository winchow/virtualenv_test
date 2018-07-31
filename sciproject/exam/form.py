from django import forms

class NameForm(forms.Form):
    sub_id = forms.CharField(label='sub_id',max_length=5) ##CS301,CS401
    academic_year = forms.CharField(label='Academic_year', min_length=6) ##2/2560
    ########################################################### total student amount
    TotalStu1 = forms.CharField(label='TotalStu1', max_length=100)
    TotalStu2 = forms.CharField(label='TotalStu2', max_length=100)
    TotalStu3 = forms.CharField(label='TotalStu3', max_length=100)
    TotalStu4 = forms.CharField(label='TotalStu4', max_length=100)
    TotalStu5 = forms.CharField(label='TotalStu5', max_length=100)
    TotalStu6 = forms.CharField(label='TotalStu6', max_length=100)
    TotalStu7 = forms.CharField(label='TotalStu7', max_length=100)
    TotalStu8 = forms.CharField(label='TotalStu8', max_length=100)
    TotalStu9 = forms.CharField(label='TotalStu9', max_length=100)
    TotalStu10 = forms.CharField(label='TotalStu10', max_length=100)
    ########################################################### instructor name
    myInput1 = forms.CharField(label='myInput1',max_length=100)
    myInput2 = forms.CharField(label='myInput2',max_length=100)
    myInput3 = forms.CharField(label='myInput3',max_length=100)
    myInput4 = forms.CharField(label='myInput4',max_length=100)
    myInput5 = forms.CharField(label='myInput5',max_length=100)
    myInput6 = forms.CharField(label='myInput6',max_length=100)
    myInput7 = forms.CharField(label='myInput7',max_length=100)
    myInput8 = forms.CharField(label='myInput8',max_length=100)
    myInput9 = forms.CharField(label='myInput9',max_length=100)
    myInput10 = forms.CharField(label='myInput10',max_length=100)
    ########################################################## instructor ratio
    ratio1 = forms.DecimalField(label='ratio1',max_digits=7, decimal_places=4)
    ratio2 = forms.DecimalField(label='ratio2',max_digits=7, decimal_places=4)
    ratio3 = forms.DecimalField(label='ratio3',max_digits=7, decimal_places=4)
    ratio4 = forms.DecimalField(label='ratio4',max_digits=7, decimal_places=4)
    ratio5 = forms.DecimalField(label='ratio5',max_digits=7, decimal_places=4)
    ratio6 = forms.DecimalField(label='ratio6',max_digits=7, decimal_places=4)
    ratio7 = forms.DecimalField(label='ratio7',max_digits=7, decimal_places=4)
    ratio8 = forms.DecimalField(label='ratio8',max_digits=7, decimal_places=4)
    ratio9 = forms.DecimalField(label='ratio9',max_digits=7, decimal_places=4)
    ratio10 = forms.DecimalField(label='ratio10',max_digits=7, decimal_places=4)

    sid = forms.CharField(label='sid', max_length=10)
    radio = forms.CharField(label='sid', max_length=10)

    test_type = forms.CharField(label='test_type',max_length=1)
    instructor_type = forms.CharField(label='instructor_type',max_length=1)
    