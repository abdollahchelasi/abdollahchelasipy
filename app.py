import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="عبدالله چلاسی - طراح و برنامه نویس",page_icon="images/a.jpg",layout="wide")




with open('c.css') as f:
    st.markdown(f"<style> {f.read()} </style>",unsafe_allow_html=True)











selected = option_menu (
    menu_title=None,
    options=["تماس با ما","صفحه اصلی"],
    icons=["envelope","house" ],
    menu_icon="cast",
    default_index=1,
    orientation="horizontal",
    styles={

        
        "nav-link":{
            'font-family': 'Courier New' 'Courier' 'monospace'
        },
        
    }
)



st.markdown("[🖥 فروشگاه آموزشی دیجی کد 🖥](https://digicode.streamlit.app/)")



if selected == "صفحه اصلی":
    
    with st.container():
        left_column,right_column = st.columns(2)
        with left_column:
#             st.error("""
# طراحی سایت با بهترین کیفیت در کمترین زمان    """)
            st.markdown("# :rainbow[طراحی سایت با بهترین کیفیت در کمترین زمان]")
            st.write("##")
            st.write("""
            """)
            st.video('abdollah.mp4')
            st.video('a.mp4')

        with right_column:
            st.divider()
            st.success("ABDOLLAH CHELASI")
            st.divider()
            st.image("https://cdn.dribbble.com/users/1118376/screenshots/3604186/developer-dribbble.gif")

    
    with st.container():
        st.write("---")
        st.success("نمونه کارهای من")
        st.write("##")
        
        c1 , c2 = st.columns(2)

        with c1:
    
            
            if st.text_input("< CYBER SECURITY >") == "@":
    
                st.markdown("[💻 Followers + Instagram 💻](https://followers.streamlit.app/)")



        st.divider()



        col1,col2,col3=st.columns((3))

        with col1:
            with st.expander(" فروشگاه جواهری رز" ,expanded=True):
                st.image("images/roz.png")
                st.write("""
    زیورآلات رز یکی از بهترین جواهرات و طلافروشی ها با بهترین محصولات و مناسب ترین قیمت در جزیره زیبای قشم می باشد.    """)
                st.markdown("[Rose jewelry](https://roz.vercel.app)")
        
        with col1:
            with st.expander(" فروشگاه دیجی کد " ,expanded=True):
                st.image("images/digicode.png")
                st.write("""
                         فروشگاه آموزشی دیجی کد با کلی سورس های آماده و اینکه بتونم با کدهای کمتری یک برنامه کامل بسازم و اینکه سعی میکنم کسانی که برنامه نویسی بلد نیستن و علاقه دارن همچین پروژه هایی بسازن و نمیخوان خیلی درگیر برنامه نویسی باشن پروژه هایی که با علامت ✨ روی پروژه ها برچسب زده شده رو اینجور پروژه ها برنامه های کامل زده شده و کد کمتری دارن
                         """)
                st.markdown("[دیجی کد](https://digicode.streamlit.app/)")
        
        with col2:

            with st.expander("وب سایت خدمات پی وی سی - رمکان",expanded=True):
                st.image("images/pvc.png")
                st.write("""
    اجرای نصب پی وی سی در سراسر جزیره قشم        """)
                st.markdown("[Pvc-Ramkan](http://pvcahmad.ir)")
            

        
        with col2:

            with st.expander("VeTube",expanded=True):
                st.image("images/hotel.png")
                st.write("""
            VeTube - Garden City Hotel Dubai
""")
                st.markdown("[VeTube - Dubai](http://vetube.streamlit.app)")
            
    


        with col3:
                with st.expander("دکوراسیـون شادمان - رمکان" ,expanded=True):
                    st.image("images/upvc.png")
                    st.write("""
    تولیدی درب و پنجره یو پی وی سی نوین ترک , فروش و نصب پی وی سی , طراحی یا ساخت و اجرای انواع سایبان پی وی سی        """)
                    st.markdown("[Dekorasion Shademan](http://pvcshademan.ir)")
        
        
        


        with col1:
            
                

            with st.expander("دکوراسیون لنج محمد" ,expanded=True):
                st.image("images/dekor.png")
                st.write("""
                             خدمات دکوراسیون لنج
                             """)
                col1,col2=st.columns([2,3])
                with col1:
                    st.markdown("[DekorLenj](https://dekorlenj.ir/)")
                        
                with col2:
                        
                    st.markdown("[LenjDekor](https://lenjdekor.streamlit.app/)")
                        
                       
                       

        col1,col2=st.columns((2))

        with col1:
            with st.expander("خدمات اینترنتی طالب" ,expanded=True):
                st.image("images/taleb.png")
                st.write("""
    خدمات نمایندگی طالب با نصب اولیه وای فای رایگان و شارژ اینترنتی اینترنتی و فروش تجهیزات وای فای با قیمت های مختلف در سراسر جزیره قشم    """)
                st.markdown("[Taleb internet services](https://taleb.vercel.app/)")
        

        with col2:
            with st.expander("عمر الزبير المرزوقي" ,expanded=True):
                st.image("images/omar.png")
                st.write("""
    اول حكم يكسر قاعدة احتكار حكام أوربا على نهائيات كاس العالم لكرة اليد """)
                st.markdown("[عمر الزبير المرزوقي](https://omarzubair.vercel.app/)")
        
            with col2:
                with st.expander("Mazaya Car Rental, Dubai" ,expanded=True):
                    st.image("images/mazaya.png")
                    st.write("""
    🇦🇪 اجاره ماشین مازایا، دبی 🇦🇪    """)
                    st.markdown("[Mazaya Car Rental Dubai](https://mazaya-cars.vercel.app/)")
        
            
            with col1:

                with st.expander("⚽ باشگاه دلفین گربدان ⚽" ,expanded=True):
                    st.image("images/gorbedan.png")
                    st.write("""
    باشگاه فوتبال دلفین گربدان یکی از پرافتخارترین و پرطرفدارترین باشگاه های جزیره قشم است. دلفین گربدان قبل از انقلاب ستاره جنوب گربدان نامیده می شد. این باشگاه اکنون در دسته دوم قشم قرار دارد. دلفین گربدان در سال 1324 در جزیره قشم روستای گربدان تأسیس شد. قرار داده شده است        """)
                    st.markdown("[Delfin Gorbadan](https://gorbedan.vercel.app)")
        
            
                       
                        
            with col1:

                with st.expander("دکوراسیون شادمان" ,expanded=True):
                    
                    st.image("images/sh.png")
                    st.write("""
                             دکوراسیون شادمان
                             """)
                    
                    st.markdown("[shademan](https://pvcshademan.streamlit.app/)")
                        
                    
            with col2:

                with st.expander("نقاش علی اکبر بندرعباس" ,expanded=True):
                    
                    st.image("images/naqash.png")
                    st.write("""
                             خدمات نقاشی علی اکبر در سر تا سر بندرعباس
                             """)
                    
                    st.markdown("[aliakbar](https://aliakbar.streamlit.app/)")
                                
                    
        

            with col2:

                with st.expander("خبر3" ,expanded=True):
                    
                    st.image("images/kh.png")
                    st.write("""
                             آخرین خبرهای ورزشی رو دنبال کنید
                             """)
                    
                    st.markdown("[Khabar3](https://khabar3.onrender.com/)")
                        
                    








if selected == "تماس با ما":
    

    with st.container():

        

        
        
       

        st.header("درباره من")

        imgabdollah , abdollah = st.columns(2)

        with imgabdollah:

            st.image("images/a.jpg",caption="00989335825325",width=200)

        with abdollah:

            st.header("عبداالله چلاسی")

            st.write("""
    من متولد 1373 قشم - روستای گربدان هستم که در زمینه طراحی وب , دسکتاپ و برنامه نویسی موبایل فعالیت دارم و به صورت آزاد یا همون فریلنسینگ کار میکنم, یکی از اتفاقات جالب زندگیم اینه که تفریحم و شغلم یکی هستند و اونم چیزی نیست جز توسعه وب و اپلیکیشن , این داستان از سال 1391 شروع شد که به سمت تکنولوژی و دنیای برنامه نویسی پا گذاشتم همچنان این سابقه با گذر زمان همچنان بیشتر و بیشتر میشه، چون برنامه نویسی چیزی هست که من باهاش دنیا رو می بینم، می سنجم و حس میکنم،و سعی ام بر این است که با همین روند پیش برم و روز به روز با تکنولوژی های جدید دنیای برنامه نویسی کار کنم و تجربیات جدیدی کسب کنم         """)

    



# -------CONTACT-------

    with st.container():
        
        st.write("---")
        st.header("تماس با من")
        st.write("##")

        st.text("برای سفارش پروژه تماس یا پیام ارسال کنید")

        col1,col2=st.columns(2)
        with col1:
            
            st.markdown("[📞 تماس](tel:00989335825325)")
            
        with col2:
            
            st.markdown("[💬 ارسال پیام](sms:00989335825325)")

        contact_form="""
        <form action="https://formsubmit.co/abdollah.chelasi@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="نام شما" required>
        <input type="email" name="email" placeholder="ایمیل شما" required>
        <textarea name="message" placeholder=" شماره تماس "  required ></textarea>
        <button type="submit">ارسال</button>
        </form> 
        """

        left , right = st.columns(2)

        with left:
            st.markdown(contact_form,unsafe_allow_html=True)

        with right:
            st.empty()
            
            
            


st.divider()

st.markdown("[وبسایت متعلق به عبدالله چلاسی میباشد.](https://abdollahchelasi.ir)")
