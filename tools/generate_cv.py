"""Render the supplied CV text into the site's two-page PDF; requires ReportLab."""
from pathlib import Path
from html import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
import argparse

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--font', default='C:/Windows/Fonts/segoeui.ttf')
parser.add_argument('--bold-font', default='C:/Windows/Fonts/segoeuib.ttf')
args = parser.parse_args()
pdfmetrics.registerFont(TTFont('CV', args.font))
pdfmetrics.registerFont(TTFont('CV-Bold', args.bold_font))
pdfmetrics.registerFontFamily('CV', normal='CV', bold='CV-Bold')
body = ParagraphStyle('body', fontName='CV', fontSize=9, leading=12, spaceAfter=4, textColor=colors.HexColor('#26231D'))
heading = ParagraphStyle('section', parent=body, fontName='CV-Bold', fontSize=11, leading=14, spaceBefore=10, spaceAfter=6, textColor=colors.HexColor('#885026'))
title = ParagraphStyle('title', parent=body, fontName='CV-Bold', fontSize=23, leading=28, alignment=TA_CENTER, spaceAfter=8)
contact = ParagraphStyle('contact', parent=body, fontSize=9, leading=13, alignment=TA_CENTER, spaceAfter=2)
bullet = ParagraphStyle('bullet', parent=body, leftIndent=10, firstLineIndent=-8, spaceAfter=3)
story = [Paragraph('Parand Khalili', title), Paragraph('<link href="mailto:parandkhalili@aut.ac.ir">parandkhalili@aut.ac.ir</link> | <link href="https://www.linkedin.com/in/parand-khalili-4428552b6">LinkedIn</link> | <link href="https://github.com/Parand1khalili">GitHub</link> | <link href="https://parand1khalili.github.io/">Website</link>', contact)]

def section(name):
    story.append(Paragraph(name, heading))

def p(text, style=body):
    story.append(Paragraph(text, style))

def entry(name, date, subtitle=None, bullets=()):
    lines = [Paragraph(f'<b>{name}</b> | {date}', body)]
    if subtitle:
        lines.append(Paragraph(subtitle, body))
    for text in bullets:
        lines.append(Paragraph('• '+text, bullet))
    story.append(KeepTogether(lines))

section('Education')
entry('Amirkabir University of Technology (Tehran Polytechnic)', 'Sep 2022 - Present', 'B.Sc. in Computer Engineering | GPA: 18.47/20', ['Undergraduate thesis: A Structure-Aware LLM-Based Framework for Graph Node Labeling.'])
section('Research Interests')
for text in [
    '<b>Graph Machine Learning:</b> Representation learning and node classification on text-attributed graphs; combining structural and semantic signals.',
    '<b>LLM-Augmented, Data-Efficient Learning:</b> Pseudo-label generation, active sample selection, and learning with limited human annotations.',
    '<b>Reliable ML and Evaluation:</b> Failure analysis, uncertainty in LLM-generated labels, calibration, and leakage-aware experimental design.',
    '<b>Data Mining and Applied ML:</b> Pattern discovery and predictive modeling for real-world, decision-oriented datasets.'
]: p('• '+text, bullet)
section('Research Experience')
entry('Undergraduate Thesis Research - LLMs for Graph Node Classification', '2026 - Present', 'Supervisor: Dr. Mostafa Haghir Chehreghani, Amirkabir University of Technology', [
    'Implemented and extended an LLM-to-GNN node-classification workflow inspired by published label-free methods; examined prompts incorporating real one- and two-hop graph evidence on Cora and CiteSeer.',
    'Conducted controlled prompt comparisons, examining pseudo-label accuracy, confidence, and downstream GCN behavior; currently preparing a matched FeatProp-based evaluation.'
])
entry('Related Investigation - LLM Annotation Failures and Reliability', 'Ongoing', 'Exploratory direction emerging from the undergraduate thesis', ['Examining failed and conflicting LLM node annotations, confidence limitations, and evaluation pitfalls; developing an interface to inspect thesis-workflow outputs (in progress).'])
section('Honors &amp; Awards')
entry('National University Entrance Examination (Konkour), Iran', '2022', 'Ranked 134 among more than 150,000 participants nationwide.')
section('Teaching Experience')
entry('Head Teaching Assistant - Business Intelligence', 'Fall 2025', 'Instructor: Dr. Ahmadi', ['Developed teaching materials and course projects; taught Power BI, Python, SQL, and analytics data modeling.'])
for text in [
    'Data Mining | Dr. Nazerfard | Spring 2026',
    'Software Engineering II (Advanced) | Dr. Gohari | Spring 2026',
    'Theory of Languages &amp; Automata | Dr. Zakeri | Fall 2025',
    'Software Engineering I | Dr. Alirezaei | Spring, Fall 2025',
    'Applied Linear Algebra | Dr. Haghir Chehreghani / Dr. Nazerfard | Fall 2024; Spring/Fall 2025',
    'Microprocessor &amp; Assembly Language | Dr. Farbeh | Fall 2025',
    'Computer Architecture | Dr. Farghadan | Spring 2025',
    'Advanced Programming | Dr. Zeinali | Spring 2024'
]: p(text)
story.append(PageBreak())
section('Professional Experience')
entry('Retail Data Analyst - EMRC', 'Jul 2026 - Present', bullets=[
    'Develop analytical dashboards and client-facing reports using real-world retail data, translating business requirements into performance indicators and actionable insights.',
    'Collaborate directly with clients to clarify reporting needs, communicate findings, and refine analytical deliverables; contribute to the ongoing automation of recurring reporting workflows.',
    'Independently developed a retail sales forecasting system using statistical methods, CatBoost, and ensemble models, with feature engineering, historical backtesting, and WAPE-based evaluation across forecast horizons.',
    'Built an interactive forecasting interface for configuring predictions, visualizing results, and exporting reports; analyzed model errors across product and geographic segments.'
])
entry('Data Analysis &amp; BI Intern - YAS Arghavani System Engineering Co.', 'Summer 2025', 'Bank Mellat IT Holding', [
    'Built Power BI dashboards to monitor POS performance, maintenance, and operational efficiency.',
    'Modeled transactional data using Power Query and DAX for revenue KPIs; integrated CRM and payment-system data to improve reporting access.'
])
section('Selected Technical Projects')
entry('<link href="https://github.com/Parand1khalili/credit-scoring-risk-mitigation">Credit Scoring &amp; Loan Default Risk Mitigation</link>', '2026', 'Python, scikit-learn', ['Built an ML pipeline with target encoding and engineered financial features to address class imbalance; tuned a Random Forest model achieving 87.41% accuracy, 79.21% balanced accuracy, and 4.65 decile lift in the reported evaluation.'])
entry('<link href="https://github.com/Parand1khalili/Fundamentals-of-AI">Artificial Intelligence Portfolio</link>', '2025', 'Python, NumPy', ['Implemented search and game-playing agents (A*, minimax/alpha-beta), constraint solving (CSP/AC-3), Q-learning, and Bayesian-network inference (Gibbs sampling and likelihood weighting).'])
entry('<link href="https://github.com/Parand1khalili/MLP-Classifier-MyTorch-Framework">MyTorch - Neural Network Components</link>', '2025', 'Python, neural networks', ['Implemented tensor operations, backpropagation, activation functions, and stochastic gradient descent in an educational neural-network framework.'])
entry('<link href="https://github.com/Parand1khalili/Fundamentals-of-AI/tree/main/06-Tetris-Genetic-Algorithm">Tetris AI via Genetic Algorithms</link>', '2025', 'Python, Pygame', ['Developed an autonomous Tetris agent with evolutionary selection, crossover, and mutation; designed a board-evaluation fitness function and visualized training.'])
entry('<link href="https://github.com/Parand1khalili/xv6_syscall">xv6 Operating System Enhancements</link>', '2025', 'C, Linux, Docker', ['Added custom system calls and multithreading support, working with memory management and process scheduling in xv6.'])
section('Technical Skills')
for text in [
    '<b>Programming:</b> Python, C++, C, Java, SQL',
    '<b>Machine Learning &amp; Research:</b> PyTorch, PyTorch Geometric, scikit-learn, GCNs, graph node classification, active learning, LLM prompting, experimental evaluation',
    '<b>Data &amp; BI:</b> NumPy, Pandas, Matplotlib, Power BI, DAX, Power Query, data modeling',
    '<b>Development Tools:</b> Git, Linux, Docker'
]: p(text)
section('Certifications')
p('Data Analysis Certificate, Quera | Summer 2025')
p('Advanced Python Bootcamp, Sematec | Sep-Dec 2024')
section('Languages &amp; Test Scores')
p('Persian (native) | English: TOEFL iBT 5/6 (CEFR C1)<br/>Reading 5, Listening 6, Writing 5, Speaking 4.5')

def footer(canvas, doc):
    canvas.setFont('CV', 8)
    canvas.setFillColor(colors.HexColor('#655B4B'))
    canvas.drawRightString(A4[0]-38, 22, f'Parand Khalili | {doc.page}')

doc = SimpleDocTemplate(str(ROOT/'assets/Parand_Khalili_CV.pdf'), pagesize=A4, rightMargin=38, leftMargin=38, topMargin=28, bottomMargin=32, title='Parand Khalili - Curriculum Vitae', author='Parand Khalili')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
