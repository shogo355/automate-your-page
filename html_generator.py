#What are the input? list for lesson, lesson number to generate, address of css refer
#list_for_lesson2=[[lesson title[name,explanation]]]
list_for_lesson2=[['2.1 Introduction to "Serious" Programming',[['Computer','A computer is a universal machine. You can program it to do any computation. It is unlike other machines like a toaster or a car(These machines can do a few things).'],
                   ['Program','The program gives you a way to tell the computer what steps to take. Any application running on the computer is programmed.'],
                   ['Programming languages','A programming language is a language that programmer can tell the computer what to do. The reason you need programming language instead of natural languages like English, is because natural languages are inherently ambiguous. Computers cannot interpret ambiguous words. Thus you need more procise language which do not allow ambiguity.'],
                   ['Interpreter','A interpreter translate the computer program to machine language(the language which machine can understand but difficult for you) simultaneously with the execution of the program. Python is the one of the language that have interpreter when they execute.'],
                   ['Python','Python is a program language that can be excuted using interpreter. It has high readability compare to other programming languages.'],
                   ['Grammar','Programming language have grammar as natural language. One of the difference explained in programming language section was that it does not allow ambiguity. The other difference is that it must be always correct. In natural language people can understand you even if you make mistake in the grammer. But computer cannot interpret that is wrong. So they try to execute the code literally which ends up with errors.']]],
                  ['lesson title',[['name','explanation']]]]

lesson_number=1
page=''
css='"reflection_validated.css"'


def generate_contents(lesson_number_in_list,list_for_lesson): #create html of contents
    contents_list=list_for_lesson[lesson_number_in_list][1]
    contents=''
    for s in contents_list:#s[0]=Computer
        if s[0]!=contents_list[0][0]:#distinguish wether the break line is necessary or not.
            contents+='''
                <HR align="center" width="90%">
'''
        contents+='''                   <h3 class="idea">'''+s[0]+'''</h3>'''#add name
        contents+='''
                <p>
                '''+s[1]+'''
                </p>'''#add explanation
    return contents

def output_html(lesson_num, list_for_lesson,html):    
    lesson_number_in_list=lesson_num-1
    contents=generate_contents(lesson_number_in_list,list_for_lesson)
    head='''<!DOCTYPE html>
<html>
 	<head>
 		<link rel="stylesheet" href='''+css+'''>
 		<title>'''+list_for_lesson[lesson_number_in_list][0]+'''</title>
 	</head>
 	'''#generate head
    body='''<body>
 			<h1 class="top"> Key points "Telling Computers What to Do"</h1>
 			<div class="contents"> <!--A box for contents-->
 				<h2 class="lesson"><u>'''+list_for_lesson[lesson_number_in_list][0]+'''</u></h2>'''+contents+'''
                </body>

 </html>'''#generate body
    return head+body

print output_html(lesson_number,list_for_lesson2,page)
