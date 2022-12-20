
from tkinter import OptionMenu
import streamlit as st
import sys
from emailhandler import email_alert
import voice_handler as vh
import speech_recognition as sr
# import email_handler as eh
from time import sleep


# st.sidebar.title("Speech Recognition System")
st.title("Speech Recognition System")
nav = st.sidebar.selectbox("Slide bar",["Home","Mic","Contact us"])
if nav == "Home":
    # st.image("rendered.jpg",width = 800)

    # col1, col2 = st.columns( [0.3, 0.9])
    # with col1:               # To display the header text using css style
    #     # st.markdown(""" <style> .font {
    #     # font-size:35px ; font-family: 'montserrat'; color: #FF9633;} 
    #     # </style> """, unsafe_allow_html=True)
    #     # st.markdown('<p class="font">About the Project</p>', unsafe_allow_html=True)
        
        
    # with col2:               # To display brand logo
        
        
    #   st.write("When it comes to project planning and management, Gantt chart is a very popular and helpful visual for project managers and teams to plan and track project roadmap, schedules, and progress. Gantt charts illustrate a project’s tasks, timelines, and other information by listing the tasks to be performed on the vertical axis, and start and finish dates on the horizontal axis.")    
    
    st.markdown(""" <style> .font {
     font-size:35px ; font-family: 'montserrat'; color: #FF9633;} 
     </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About the Project</p>', unsafe_allow_html=True)

    st.write("Our System mainly focuses on recognizing stationary words from a given speech input.The system is developed using speech recognition using Machine Learning models")



    st.image("tts.jpeg",width = 800)




if nav == "Mic":


    def read() :
        engine = vh.init_engine()
        voice = vh.get_voice(engine)
        vh.speak("Hello, do you want to add groceries or send the list?", voice, engine)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("lexi :  Talk,i am listening...")
            audio = r.record(source, duration=2)

        choice = r.recognize_google(audio, language='en-US')
        st.write(choice)

        if "i want to add" in str(choice).lower():
            vh.speak("Let me know what you want to add?", voice, engine)
            while True:
                try:
                    vh.speak("uh-huh!", voice, engine)
                    addition = vh.get_audio()
                    if "over" in str(addition).lower():
                        break
                    st.write(addition)
                    f = open("shooping_list.txt", "a")
                    f.write("Me : "+addition + "\n")
                    f.close()
                except:
                    st.write("Try again")
        # elif "send" in choice:
        #     vh.speak("Sending the current list to your email", voice, engine)
        #     with open ("shooping_list.txt", "r") as file:
        #         shopping_list = file.read()
        #         eh.email_alert('Shopping list', shopping_list)
        else:
            vh.speak("Please restart me. I am still not that complicated", voice, engine)
            sys.exit()


    def display():
        f = open("shooping_list.txt", "r")
        for i in f.readlines():
            st.write(i)

    def send():
        f = open("shooping_list.txt", "r")
        message = ""
        for i in f.readlines():
            message += i

        email_alert("Shopping list", message)


    st.button("Shopping List", on_click=display,)

    st.button("Talk", on_click=read,)

    button_style = """
        <style>
        .stButton > button {
            color: black;
            background: cyan;
            width: 200px;
            height: 50px;
        }
        </style>
        """
    st.markdown(button_style, unsafe_allow_html=True)


    st.button("Send", on_click=send,)

if nav == "Contact us":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
        #st.write('Please help us improve!')
        Name=st.text_input(label='Please Enter Your Name') #Collect user feedback
        Email=st.text_input(label='Please Enter Your Email') #Collect user feedback
        Message=st.text_input(label='Please Enter Your Message') #Collect user feedback
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')




# with st.sidebar:
#     choose = OptionMenu("App Gallery", ["About", "Project Planning", "Contact"],
#                          icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
#                          menu_icon="app-indicator", default_index=0,
#                          styles={
#         "container": {"padding": "5!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"}, 
#         "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "#02ab21"},
#     }
#     )

# if choose == "About":

#     col1, col2 = st.columns( [0.3, 0.7])
#     with col1:               # To display the header text using css style
#         st.markdown(""" <style> .font {
#         font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
#         </style> """, unsafe_allow_html=True)
#         st.markdown('<p class="font">About the Project</p>', unsafe_allow_html=True)
        
#     with col2:               # To display brand logo
        
#         # st.image(logo, width=130 )
#       st.write("When it comes to project planning and management, Gantt chart is a very popular and helpful visual for project managers and teams to plan and track project roadmap, schedules, and progress. Gantt charts illustrate a project’s tasks, timelines, and other information by listing the tasks to be performed on the vertical axis, and start and finish dates on the horizontal axis.")    
#     # st.image(profile, width=700 )



# elif choose == "Project Planning":
# #Add a file uploader to allow users to upload their project plan file
#     st.markdown(""" <style> .font {
#     font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
#     </style> """, unsafe_allow_html=True)
#     st.markdown('<p class="font">Upload your project plan</p>', unsafe_allow_html=True)

    
        
        

# def read() :
#     engine = vh.init_engine()
#     voice = vh.get_voice(engine)
#     vh.speak("Hello, do you want to add groceries or send the list?", voice, engine)
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("UDAY :  Talk,i am listening...")
#         audio = r.record(source, duration=2)

#     choice = r.recognize_google(audio, language='en-US')
#     st.write(choice)

#     if "i want to add" in str(choice).lower():
#         vh.speak("Let me know what you want to add?", voice, engine)
#         while True:
#             try:
#                 vh.speak("aha!", voice, engine)
#                 addition = vh.get_audio()
#                 if "done" in str(addition).lower():
#                     break
#                 st.write(addition)
#                 f = open("shooping_list.txt", "a")
#                 f.write("Me : "+addition + "\n")
#                 f.close()
#             except:
#                 st.write("Try again")
#     # elif "send" in choice:
#     #     vh.speak("Sending the current list to your email", voice, engine)
#     #     with open ("shooping_list.txt", "r") as file:
#     #         shopping_list = file.read()
#     #         eh.email_alert('Shopping list', shopping_list)
#     else:
#         vh.speak("Please restart me. I am still not that complicated", voice, engine)
#         sys.exit()



# def display():
#     f = open("shooping_list.txt", "r")
#     for i in f.readlines():
#         st.write(i)

# def send():
#     f = open("shooping_list.txt", "r")
#     message = ""
#     for i in f.readlines():
#         message += i

#     email_alert("Shopping list", message)


# st.button("Shopping List", on_click=display,)

# st.button("Talk", on_click=read,)

# st.button("Send", on_click=send,)
