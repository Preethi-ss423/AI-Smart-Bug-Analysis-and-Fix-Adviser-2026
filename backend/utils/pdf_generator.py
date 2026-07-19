from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase.pdfmetrics import stringWidth

from datetime import datetime
import random
def generate_pdf(report_data):

    file_path = "Bug_Analysis_Report.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER
    title_style.textColor = colors.darkblue

    heading_style = styles["Heading1"]
    heading_style.textColor = colors.darkblue

    sub_heading = styles["Heading2"]

    body_style = styles["BodyText"]

    content = []
    content.append(
        Paragraph(
            "AI SMART BUG ANALYSIS & FIX ADVISER",
            title_style
        )
    )

    content.append(
        Paragraph(
            "AI Powered Bug Analysis, Root Cause Detection & Fix Suggestions",
            body_style
        )
    )

    content.append(Spacer(1,20))
    report_id = "BUG-" + str(random.randint(1000,9999))

    current_time = datetime.now().strftime(
        "%d %B %Y %I:%M %p"
    )

    content.append(
        Paragraph(
            "<b>Report Generated:</b> " + current_time,
            body_style
        )
    )

    content.append(
        Paragraph(
            "<b>Analysis ID:</b> " + report_id,
            body_style
        )
    )

    content.append(Spacer(1,20))
    bug = report_data.get("bug_info", {})

    log = report_data.get("log_analysis", {})

    duplicate = report_data.get("duplicate", {})

    root = report_data.get("root_cause", {})

    fix = report_data.get("fix", {})
    content.append(
        Paragraph(
            "BUG INFORMATION",
            heading_style
        )
    )

    content.append(Spacer(1,10))

    bug_table = [

        ["Bug Title",
         bug.get("title","")],

        ["Description",
         bug.get("description","")],

        ["Uploaded File",
         bug.get("uploaded_file","No File")]

    ]
    table = Table(
        bug_table,
        colWidths=[140,320]
    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(0,-1),colors.lightblue),

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8),

            ("VALIGN",(0,0),(-1,-1),"TOP")

        ])

    )

   
    content.append(Spacer(1,8))

    if isinstance(log, dict):

        log_table = []

        for key, value in log.items():

            log_table.append([
                str(key).replace("_"," ").title(),
                str(value)
            ])

        table = Table(
            log_table,
            colWidths=[170,290]
        )

        table.setStyle(

            TableStyle([

                ("BACKGROUND",(0,0),(0,-1),colors.lightgrey),

                ("GRID",(0,0),(-1,-1),1,colors.grey),

                ("BOTTOMPADDING",(0,0),(-1,-1),8),

                ("TOPPADDING",(0,0),(-1,-1),8)

            ])

        )

        content.append(table)

    else:

        content.append(
            Paragraph(
                str(log),
                body_style
            )
        )

    content.append(Spacer(1,18))
    content.append(
        Paragraph(
            "ROOT CAUSE ANALYSIS",
            heading_style
        )
    )

    content.append(Spacer(1,8))

    
    if isinstance(fix, dict):

     content.append(
        Paragraph(
            "<b>Agent:</b> " + fix.get("agent",""),
            body_style
        )
    )

    content.append(
        Paragraph(
            "<b>Exception:</b> " + fix.get("exception",""),
            body_style
        )
    )

    content.append(Spacer(1,10))

    content.append(
        Paragraph(
            "<b>Recommendations</b>",
            sub_heading
        )
    )

    for recommendation in fix.get("recommendations",[]):

        content.append(
            Paragraph(
                "• " + recommendation,
                body_style
            )
        )

    content.append(Spacer(1,18))
    content.append(

        Paragraph(

            "DUPLICATE BUG DETECTION",

            heading_style

        )

    )

    content.append(Spacer(1,8))

    if isinstance(duplicate, list):

     for bug in duplicate[:3]:

        content.append(
            Paragraph(
                "<b>" + bug.get("bug_id","") + "</b>",
                sub_heading
            )
        )

        content.append(
            Paragraph(
                "Title : " + bug.get("title",""),
                body_style
            )
        )

        content.append(
            Paragraph(
                "Severity : " + bug.get("severity",""),
                body_style
            )
        )

        content.append(
            Paragraph(
                "Resolution : " + bug.get("resolution",""),
                body_style
            )
        )

        content.append(
            Spacer(1,10)
        )

        content.append(Spacer(1,18))
  # ---------------- AI FIX SUGGESTIONS ----------------
    # ---------------- AI FIX SUGGESTIONS ----------------

    content.append(
        Paragraph(
            "AI FIX SUGGESTIONS",
            heading_style
        )
    )

    content.append(Spacer(1, 8))

    if isinstance(fix, dict):

        # Agent Name
        content.append(
            Paragraph(
                "<b>Agent:</b> " + str(fix.get("agent", "")),
                body_style
            )
        )

        # Exception
        content.append(
            Paragraph(
                "<b>Exception:</b> " + str(fix.get("exception", "")),
                body_style
            )
        )

        content.append(Spacer(1, 10))

        # Recommendations Heading
        content.append(
            Paragraph(
                "<b>Recommendations</b>",
                sub_heading
            )
        )

        recommendations = fix.get("recommendations", [])

        if recommendations:

            for recommendation in recommendations:

                content.append(
                    Paragraph(
                        "• " + str(recommendation),
                        body_style
                    )
                )

        else:

            content.append(
                Paragraph(
                    "No recommendations available.",
                    body_style
                )
            )

    else:

        content.append(
            Paragraph(
                str(fix),
                body_style
            )
        )

    content.append(Spacer(1, 25))

    # ---------------- FOOTER ----------------

    line = "_" * 90

    content.append(
        Paragraph(
            line,
            body_style
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "<b>Generated By</b>",
            sub_heading
        )
    )

    content.append(
        Paragraph(
            "AI Smart Bug Analysis & Fix Adviser",
            body_style
        )
    )

    content.append(
        Paragraph(
            "Multi-Agent AI System",
            body_style
        )
    )

    content.append(Spacer(1, 5))

    content.append(
        Paragraph(
            "© 2026 AI Smart Bug Analysis & Fix Adviser",
            body_style
        )
    )

    # ---------------- BUILD PDF ----------------

    doc.build(content)

    return file_path