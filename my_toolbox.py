from flask import Flask, render_template, request, redirect, url_for
from form import FormElements
import re

app = Flask(__name__)

app.config['SECRET_KEY']= 'myseckey'

'''**************************************************************
*****************************************************
*****************************'''

# My math toolbox home page

@app.route('/')
def index():
    choices = ['BMI Calculator', 'Multiplication Tables', 'Check Divisibility',
            'Check Prime Number', 'Factors of a number', 'Check Leap Year',
            'Fibonacci Series', 'HCF and LCM', 'Factorial of a Number',
            'Find x^n']
    choices.sort()
    return render_template('index.html', choices = choices)




@app.route('/choice')
def choice():
    val = request.args.get('choose')
    if val == 'BMI Calculator' :
        return redirect(url_for('bmi_home'))

    elif val == 'Multiplication Tables':
        return redirect(url_for('multi_table'))

    elif val == 'Check Divisibility':
        return redirect(url_for('div_check'))

    elif val == 'Check Prime Number':
        return redirect(url_for('prime_num'))

    elif val == 'Factors of a number':
        return redirect(url_for('factors'))

    elif val == 'Check Leap Year':
        return redirect(url_for('leap'))

    elif val == 'Fibonacci Series':
        return redirect(url_for('fib_nums'))

    elif val == 'HCF and LCM':
        return redirect(url_for('hcf_lcm'))

    elif val == 'Factorial of a Number':
        return redirect(url_for('factorial'))

    elif val == 'Find x^n':
        return redirect(url_for('power'))


'''**************************************************************
****************************************************
******************************'''


''' ##############################################################
##################################################
###############################'''

# BMI Calculator



@app.route('/body_mass_index')  # BMI home
def bmi_home():
    run = False
    return render_template('bmi.html', run=run)



@app.route('/body_mass_index/solution')   # BMI solution page
def body_mass_index():
    run = True
    weight = float(request.args.get('weight'))
    height = float(request.args.get('height'))
    bmi = weight/(height * height)
    bmi = round(bmi, 2)
    return render_template('bmi.html', bmi= bmi, run=run)

'''###################################################################
#########################################################
######################################'''







'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''

# Multiplication Table

@app.route('/multi_table', methods=['GET', 'POST'])
def multi_table():
    m_num = False

    multi_form = FormElements()

    if multi_form.validate_on_submit():

        m_num = multi_form.int_input.data

        multi_form.int_input.data = ''

    return render_template('multi_table.html', multi_form=multi_form, m_num=m_num)






'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''





'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

@app.route('/divisibility check', methods=['GET', 'POST'])
def div_check():
    run = False
    div_form = FormElements()
    div_by = 0
    div_num = 0
    if div_form.validate_on_submit():

        div_num = div_form.int_input.data
        div_by = div_form.int_input2.data
        run = True
    return render_template('divisibility_check.html', div_num= div_num,
                            run= run, div_by = div_by, div_form = div_form)


'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''




'''Function for Prime number '''


@app.route('/prime_num', methods=['GET', 'POST'])
def prime_num():
    inp_num = False
    string =''
    prime_form = FormElements()

    if prime_form.validate_on_submit():
        inp_num = prime_form.int_input.data
        if inp_num == 1:
            string = 'Neither Prime nor Composite!'
        else:
            for i in range (2,inp_num):
                if (inp_num % i) == 0:
                    string = str(inp_num) +' is NOT a prime number'
                    break
            else:
                string = str(inp_num) + ' is a prime number'
        prime_form.int_input.data = ''

    return render_template('prime.html', prime_form=prime_form, inp_num=inp_num,
                            string = string)




'''Function for factors of a number'''

@app.route('/factors', methods = ['GET', 'POST'])
def factors():
    num = False

    factor_form = FormElements()
    fac = []


    if factor_form.validate_on_submit():
        num = factor_form.int_input.data
        for i in range(1, num+1):
            if num%i==0:
                fac.append(i)


        factor_form.int_input.data = ''

    return render_template('factors.html', num=num, fac = fac,
                            factor_form=factor_form)



'''Function for leap year check'''


@app.route('/check leap year', methods = ['GET', 'POST'])
def leap():
    show = False
    year = ''
    check = ''
    leap_form = FormElements()
    if leap_form.validate_on_submit():
        show = True
        year = leap_form.int_input.data
        if year % 4 ==0:

            if year%100 == 0:

                if year % 400 == 0:
                    check = True

                else:
                    check = False
            else:
                check = True
        else:
            check = False

        leap_form.int_input.data = ''

    return render_template('leap_year.html', show=show, leap_form=leap_form,
                            year=year, check= check)




@app.route('/fibonacci numbers', methods = ['GET', 'POST'])
def fib_nums():
    terms = False
    fib_form = FormElements()
    fib_list = [1, 1]
    a1 = 1
    a2 = 1
    if fib_form.validate_on_submit():
        terms = fib_form.int_input.data
        for nums in range (3, terms +1):
            a1, a2 = a2, a1 +a2
            fib_list.append(a2)

    return render_template('fib_num.html', terms=terms,
                            fib_form=fib_form, fib_list=fib_list, a1=a1, a2=a2)



@app.route('/HCF and LCM', methods = ['GET', 'POST'])
def hcf_lcm():
    show = False;
    num1 = ''
    num2 = ''
    list1 = []
    list2 = []
    common = []
    hcf = ''
    lcm = ''
    hcf_form = FormElements()

    if hcf_form.validate_on_submit():
        show = True
        num1 = hcf_form.int_input.data
        num2 = hcf_form.int_input2.data

        for x in range(1,num1+1):
            if num1 % x == 0:
                list1.append(x)

        for x in range(1,num2+1):
            if num2 % x == 0:
                list2.append(x)

        common = [value for value in list1 if value in list2]
        hcf = max(common)
        lcm = (num1*num2)/ hcf
    return render_template('hcf_lcm.html',show = show, hcf_form=hcf_form,
                            num1=num1, num2=num2, hcf=hcf, lcm=lcm)




@app.route('/factorial of num', methods=['GET', 'POST'])
def factorial():
    show = False
    num =''
    factorial = 1

    fact_form = FormElements()

    if fact_form.validate_on_submit():
        show = True
        num = fact_form.int_input.data
        for i in range(1, num+1):
            factorial = factorial * i

    return render_template('factorial.html', show=show,
                            num=num, factorial=factorial, fact_form=fact_form)



@app.route('/power of x', methods=['GET', 'POST'])
def power():
    show = False
    x = ''
    n = ''
    ans = ''

    power_form =FormElements()

    if power_form.validate_on_submit():
        show = True
        x = power_form.int_input.data
        n = power_form.int_input2.data
        ans = x**n
    return render_template('power.html', show=show, x=x, n=n, ans=ans,
                            power_form=power_form)












if __name__ == '__main__':
    app.run(debug=False)
