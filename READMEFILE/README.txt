There will be a user in this project who will give a proposal to the company to get his 
tender approved which he can create using different templates but before that he will have
to signup or login to the website only then he can create the proposal.

In this project the project name is 'CoustomTender' and app name is 'coustmer' here are 
one user already register and his username is 'paramjeet' and password is '123456' and a superuser
name is 'admin' and password is  '1234'.

steps:-
1- first the enter in project 'CoustomTender' 
2- In local server run the server using this commomd 'python manage.py runserver'
3- open a page in front of user then user must be require signup and then login
4- without signup user not enter the website 
5- for demo a user already register and the user some data added 
6- username  = 'paramjeet' and password = '123456'
7- superuser = 'admin' and password = '1234'
8- local Host URL  http://127.0.0.1:8000/
9- 

signup criteria :-
                both password are same
                password min length should be must 8 character

1- views.py
    [In This Project We Have Diffrent Function And All Function Role Is Also Diffrent So Below Given All Function 
    Details With His Worlking Stage That A Particular Function Work When Its URL Hits To Check All Function Details To 
    Open { views.py } Here Mention All Details About The Fuction Below Given All Function Details With His Working.]


    coustmer_front(): 
            these function do work when the server is run and the user(coustmer) enter the website a front page is open 
    and in front page mention signup and login button.



    coustmer_afterlogin_front():
                        these function do work when the user(coustmer) create a acount using signup and  after created the acount
    the user is mandatory to login for  entering the website after the login process completed  the user(coustmer) enter the 
    website and create his preferred proposal.



    coustmer_preview():
                these fuction do work when the user(coustmer) entering the website after completed login process in front of 
    user(coustmer) three types of template open whereas he choose one preferred template to create his proposal and after create 
    the proposal  he click on submit button to done   the proposal. 

    

    coustmer_after_create():
                these function do work when the user(coustmer) create his preferred proposal and after created the proposal 
    anyone want to see that how is our proposal made that's  his function work properly  to which template user choose the 
    preview watch with his. 


    coustmer_signup(): 
            these function do work when the new user(coustmer) want to create proposal and want to  know about our website
    so firstly his create a acount  then create proposal and know about our website. 

    coustmer_login():
                these function do work properly  when the user(coustmer)  filled details  at the time of signing up should be 
    correct only then he will be able to login otherwise he not enter the website and exit the login page.


    coustmer_logout():
            these function do only work when user(coustmer) want to exit the website and not show his data to anyone in this
    case the user(coustmer) exit the website by using LogOut button. 


    create_proposal():
                these function do work when its URL hits and the user(coustmer) is authenticated mean that after create the 
    new proposal user muat be should login in website and now he  want to create a new  proposal  which he is choose template  
    for fill the tender as soon as he clicks on the create button a new form open in front of user(coustmer)  the user fill the 
    form and submit the data and his proposal is created. 
    

    edit_proposal(): 
                these function do work when its URL hits the user(coustmer) created a template and now he want to some changes 
    his proposal as like he want to change  Title, Number etc then he click on the edit button to change template data and after
    change the data click on the submit button as soon as he click on the submit button his updated data is created  and  he 
    can see it by clicking on the preview button.

        
    delete_proposal():
                these function do work when its URL hits the user(coustmer) created a template and now he want to delete his 
    proposal for some reason then he simply click on the delete button to delete the proposal. 


    coustmer_proposal_image():
            these function do work when its URL hits when the user(coustmer) created a proposal which template  has been used,
    this function shows us which template the user has created a proposal for, so which template can he use this data is visible 
    to us in a table form with its name, company name, created date and with proper template image.

2- Templates

    [ There are some HTML templates names and all templates do different things all details mentioned in below ]

    singup.html: 
            this is a Signup template which opens a registration form for us and the user(coustmer) completes his registration
    by filling it.


    login.html
        It's  works like  Signup template but it will login only if the user is already registered otherwise it will not happen.


    aftercreate1.html:
                If the user created a proposal using the first template, then how does it look after creating the proposal our
    these template does that work.


    aftercreate2.html:
                If the user created a proposal using the second template, then how does it look after creating the proposal 
    our these template does that work.


    aftercreate3.html:
                If the user created a proposal using the third template, then how does it look after creating the proposal 
    our these template does that work.


    base.html:
            its a base template that's work we have written the code which is required in all the templates  in this template 
    so that it can be used everywhere.


    edit.html:
        this template is used when the user has to change something in his already created data, then he can get this template 
    render and make changes in it.
            
    form.html:
        this template open a form for creating a proposal  whichever template the user clicks on, it opens the same form.


    front.html:
            its a front page of our website there are nothing to show related to proposal except about the website wikipedia 
    and some information about business proposals tender.


            
    proposal1.html:
                this is the first template which the user will see first and only then he will use it  if he likes it, otherwise 
    he will see other templates and create his proposal in preferred templates.


    proposal2.html:
                same as proposal1.html this is the second template which the user will see first and only then he will use it
    if he likes it, otherwise he will see other templates and create his proposal in preferred templates.


    proposal3.html:
                same as both template  this is the third template which the user will see first and only then he will use it 
    if he likes it, otherwise he will see other templates and create his proposal in preferred templates

