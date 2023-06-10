import base64
import streamlit as st
import gspread
from dotenv import load_dotenv
import json
import os

load_dotenv()
variables_keys = {
        "type": st.secrets["type"],
        "project_id": st.secrets["project_id"],
        "private_key_id": st.secrets["private_key_id"],
        "private_key": st.secrets["private_key"],
        "client_email": st.secrets["client_email"],
        "client_id": st.secrets["client_id"],
        "auth_uri": st.secrets["auth_uri"],
        "token_uri": st.secrets["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["client_x509_cert_url"]
    }
## Load Env variables
credentials = variables_keys
key = st.secrets["key"]

############  Import Files
with open('data/Aditya Resume.pdf', 'rb') as pdf:
    pdf_file = pdf.read()

############  Page Config
st.set_page_config(
    page_title='Aditya Wadhavane',
    page_icon="🚀",
    initial_sidebar_state="auto",
)

###########  SideBar
st.sidebar.markdown("""
    <h1 style="font-size: 50px; margin-left: 5px;">Aditya <br> Wadhavane</h1>
    """, unsafe_allow_html=True)
st.sidebar.caption("Personal Website")

st.sidebar.download_button("Download CV From Here   ", data=pdf_file)

## Navigatiob Bar
st.sidebar.write("""
<nav>
        <h2>Navigation</h2>
        <ul style="list-style: none;">
            <li><a href="#summary" style="text-decoration: none;">🧿 Summary</a></li>
            <li><a href="#experience" style="text-decoration: none;">🧿 Experience</a></li>
            <li><a href="#education" style="text-decoration: none;">🧿 Education</a></li>
            <li><a href="#skills" style="text-decoration: none;">🧿 Skills</a></li>
            <li><a href="#projects" style="text-decoration: none;">🧿 Projects</a></li>
            <li><a href="#certifications" style="text-decoration: none;">🧿 Certifications</a></li>
            <li><a href="#lets connect" style="text-decoration: none;">🧿 Lets Connect</a></li>
        </ul>
    </nav>
    """, unsafe_allow_html=True)

st.sidebar.markdown("### About Me")
st.sidebar.info("""
    🏠 Nashik Maharashtra,422101\n
    📞 920931202\n
    📧 adityaswadhavane@gmail.com
""")

###########  Main Page

######################  Summary   ######################

st.markdown('## SUMMARY', unsafe_allow_html=True)
st.info('''
- Results-driven data professional with expertise in analysis and generating actionable insights.
- Proven track record in evaluating sales performance, ramping rates, program impact assessment and recommendation. 
- Proficient in Python, SQL, and advanced Excel for building data-driven products. 
- Adept at maintaining code infrastructure and resolving production issues. 
- Strong problem-solving and communication skills for data-driven decision-making and impactful recommendations. 
- Eager to learn new technologies and seek growth opportunities. Motivated to contribute to challenging data roles. 
- Proficient in a wide range of data pipelines, processing techniques, and visualization tools .
''')

st.divider()
######################  EXPERIENCE   ######################

st.markdown('## EXPERIENCE')
st.write("""
<body>
    <div>
        <h1 style="color: #8E8FD3; font-size: 20px;">Emplay Analytics | Product Delivery Analyst</h1>
    <h2 style="color: #AAD2EF; font-size: 15px;">Oct.2021 &ndash; Present</h2>
    <ul>
        <li>Provided holistic sales enablement solutions, leveraging <strong>data-driven recommendations</strong> for deals, accounts, sales representative and products.</li>
        <li>Developed robust <strong>pipeline-based data product modules,</strong>facilitating seamless data ingestion, pre-processing, model building, and performance tracking.</li>
        <li>Built <strong>sql modules to analyze KPI metrics</strong> of high performers, empowering managers to improve underperforming individuals' sales pipelines through data-driven insights.</li>
        <li>Designed and implemented a <strong>personalized recommendation algorithm</strong> for Sales Enablement, enhancing pipeline performance for achieving sales targets.</li>
        <li>Lead various analysis for sales team including ramping rate, program impact, skill sets, and account churn using product & storytelling dashboards.</li>
        <li>Managed code infrastructure, resolved production issues, <strong>ensuring smooth functioning of analytical solutions</strong> in a demanding environment.</li>
    <p style="margin-top: 20px;margin-bottom: 30px;"><strong>Key Skills:</strong> Python, SQL, data pipelines frameworks (e.g., Kedro, Prefect), data visualization tools (e.g., Power BI, plotly, Google Data Studio), Streamlit, Excel.</h2>
    </ul>
    </div>

</body>
""", unsafe_allow_html=True)

st.write("""
<body>
    <div>
        <h1 style="color: #8E8FD3; font-size: 20px;">Energy Exemplar | Data Analyst Intern</h1>
    <h2 style="color: #AAD2EF; font-size: 15px;">Feb. 2021 &ndash; Sept. 2021</h2>
    <ul>
        <li>Built comprehensive gas and electricity datasets through <strong>web scraping</strong> and market research, enabling strategic decision-making.</li>
        <li>Automated various data scraping processes, <strong>reducing turnaround time and improving operational efficiency</strong>.</li>
        <li><strong>Developed an automation tool</strong> for efficient distance calculations, wiki page scraper in internal hackathon.</li>
    <p style="margin-top: 20px;margin-bottom: 30px;"><strong>Key Skills:</strong> Python, advanced Excel, Data Modelling, Power BI.</h2>
    </ul>
    </div>

</body>
""", unsafe_allow_html=True)

st.write("""
<body>
    <div>
        <h1 style="color: #8E8FD3; font-size: 20px;">Polycab India Ltd | Graduate Engineer Trainee</h1>
    <h2 style="color: #AAD2EF; font-size: 15px;">Feb 2019 &ndash; July 2020</h2>
    <ul>
        <li><strong>Maintained CRM data</strong>, ensuring accurate and up-to-date information for effective client tracking.</li>
        <li><strong>Monitored KPIs</strong> to optimize customer relationship management processes.</li>
        <li>Collaborated on creating and managing the annual territory plan, conducting market analysis.</li>
        <li><strong>Assisted in resolving technical issues</strong> and conducted product inspections to ensure quality and customer satisfaction.</li>
    </ul>
    </div>

</body>
""", unsafe_allow_html=True)

st.divider()
st.markdown('## EDUCATION')
st.write("""
<body>
    <div>
        <h1 style="color: #8E8FD3; font-size: 20px;">BE-Electrical | Pune University</h1>
        <h2 style="color: #AAD2EF; font-size: 15px;">2014 &ndash; 2018</h2>
        <ul>
            <li><strong>Percentage</strong>  &ndash; First Class with Distinction</li>
        </ul>
    </div>

</body>
""", unsafe_allow_html=True)

st.divider()
######################  SKILLS   ######################
st.markdown('## SKILLS')
skill1, skill2 = st.columns(2)

with skill1:
    st.write("""
    <ul>
         <li style="font-weight: bold;">Programming Languages:
             <ul>
                 <li>Python</li>
                 <li>SQL</li>
                 <li>R Programming</li>
             </ul>
         </li>
         <li style="font-weight: bold;">Web Frameworks:
             <ul>
                 <li>	</li>
                 <li>FastAPI</li>
             </ul>
         </li>
         <li style="font-weight: bold;">Data Analysis:
             <ul>
                 <li>Pandas</li>
                 <li>NumPy</li>
                 <li>Advance Excel</li>
                 <li>Advance SQL</li>
                 <li>Sklearn</li>
             </ul>
         </li>
     </ul>""", unsafe_allow_html=True)

with skill2:
    st.write("""
    <ul> <li style="font-weight: bold;">Data Pipelines:
             <ul>
					 <li>Kedro</li>
					 <li>Prefect</li>
             </ul>
         </li>
         <li style="font-weight: bold;">Data Visualization:
             <ul>
                 <li>Plotly,Matplotlib</li>
                 <li>Google Data Studio</li>
                 <li>Power BI</li>
             </ul>
         </li> 
         </ul>
    """, unsafe_allow_html=True)

st.divider()
##### Tools
st.markdown("## Tools")
st.write("""
<ul>
        <li>Version Control: Git, GitHub</li>
        <li>IDEs: Visual Studio Code, PyCharm</li>
        <li>Database: MySQL, PostgreSQL</li>
    </ul>""", unsafe_allow_html=True)

st.markdown('## PROJECTS')
tab1, tab2, tab3, tab4 = st.tabs([
    "Deal DNA Project", "Ramp Analysis", "Similarity Algorithm", "Web Scraper"])

with tab1:
    st.header("Deal DNA Project")
    st.caption("Identify drivers of success of top performers and help sales managers to improve their pipelines.")
    st.markdown("""
- Conducted EDA on multiple sales datasets using Python and SQL and Built a data model for analysis.
- Developed and maintained data pipelines using Kedro for data ingestion, preprocessing, and model building.
- Analyzed KPIs and model outputs to derive data-driven recommendations to help indivisual to give path to win deal.
- Presented insights and recommendations through interactive dashboards in Google Data Studio.
- Result: identified success factors for winning deals and increased pipeline opportunities by 20% in quarter
   """)

with tab2:
    st.header("Ramp Analysis")
    st.caption("Identify ramping rate of new hires and help managers to improve ramp rate by analysing KPIS")
    st.markdown("""
- Developed SQL modules for data preprocessing and KPI calculations.
- Analyzed multiple KPIs to determine the ramping rate of the sales team, specifically for new hires.
- Identified key factors contributing to high performance and provided guidance to underperforming individuals to improve their performance and meet their quotas.
- Generated KPI reports to assist managers in monitoring and tracking individual performance.
- Outcome: Identified ramping rates for high performers and suggested best practices to help low performers to met their quota.
      """)

with tab3:
    st.header("Similar Deales/Account recommendation Algorithm")
    st.caption(
        "Building similar entity algorithm for sales teams to learn from peers by similar deal,account or product recommendation")
    st.markdown("Will update details shortly")

with tab4:
    st.header("Webscraper tool")
    st.caption("Scraping live data from website to keep track of consumption and production of gas and electricity.")
    st.markdown("Will update details shortly")

st.divider()
st.markdown('## CERTIFICATIONS')
st.markdown("""
    - IBM Cognitive Class Badges
        - Python for Data science
        - R essentials
    - 100 days of Code: The Complete Python Pro Bootcamp (By- Dr.Angela Yu)
    - SQL-MYSQL for Data Analytics and Business 
    - Udemy Excel Essentials
    - Intellipaat Data Science Certification
    - Intellipaat SAP Certification
    - Mechatronics Course of Certification-COEP, Pune
    - Currently Pursuing - Master GPT 
""")

st.divider()
##################  Lets Connect
st.markdown("## LETS CONNECT")
# Establish connection and authenticate with Google Sheets
scope=['https://spreadsheets.google.com/feeds',
      'https://www.googleapis.com/auth/drive',
      'https://www.googleapis.com/auth/drive.file',
      'https://www.googleapis.com/auth/spreadsheets'
      ]

gs = gspread.service_account_from_dict(credentials,
                                        scopes=scope)
ws = gs.open_by_key(key)
worksheet = ws.sheet1

# Create Streamlit form
with st.form("user_form"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Your message")
    submit_button = st.form_submit_button("Send")

if submit_button:
    data = [name, email, message]
    worksheet.append_row(data)
    st.success("Thank you! We will be in touch soon.")
