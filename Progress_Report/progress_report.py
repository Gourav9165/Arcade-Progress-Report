import pandas as pd

# Load the CSV file
file_path = 'D:\\PROGRAMMING\\PYTHON TO HTML\\excel.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Print column names to verify the exact names
print("Column names in CSV:", df.columns)

# Replace NaN with "None" in the respective columns
columns_to_fill = ['Milestone Earned', 'Names of Completed Skill Badges', 'Names of Completed Arcade Games', 'Names of Completed Trivia Games']
for col in columns_to_fill:
    if col in df.columns:
        df[col] = df[col].fillna('None')

# Ensure 'Access Code Redemption Status' column exists and format the redemption status
if 'Access Code Redemption Status' in df.columns:
    def format_status(status):
        if status == "Yes":
            return '<span class="status great-job">Great👌</span>'
        else:
            return '<span class="status havent">Haven\'t😔</span>'
    
    df['Access Code Redemption Status'] = df['Access Code Redemption Status'].apply(format_status)
else:
    print("Column 'Access Code Redemption Status' not found in CSV.")

# Drop the specified columns
columns_to_drop = ['Names of Completed Skill Badges', 'User Email', 'Google Cloud Skills Boost Profile URL', 'Profile URL Status', 'Names of Completed Arcade Games', 'Names of Completed Trivia Games']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

# Sort the DataFrame by "# of Skill Badges Completed" in descending order
if '# of Skill Badges Completed' in df.columns:
    df = df.sort_values(by='# of Skill Badges Completed', ascending=False)

# Convert DataFrame to HTML with centered text
html_table = df.to_html(escape=False, index=False, classes='table table-striped', border=0, justify='center')

# Create HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Cloud Arcade Facilitator</title>
    <link rel="icon" href="faviconn.ico" type="image/x-icon">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

        body {{
            font-family: 'Montserrat', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e8eaf6;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            user-select: none;
            animation: fadeIn 0.8s ease-in-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}

        .container {{
            width: 95%;
            max-width: 1200px;
            background: linear-gradient(135deg, #ffffff, #b7b5b529);
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            overflow: hidden;
            padding: 20px;
            margin-top: 15px;
        }}

        .header {{
            display: flex;
            align-items: center;
            flex-direction: column;
            padding: 15px 0;
            background: linear-gradient(135deg, #a6cdf457, #91b9dc, #a6cdf457);
            color: #2c3e50;
            border-radius: 15px;
            position: relative;
            animation: slideIn 0.8s ease-in-out;
            text-align: center;
        }}
        
        .header .head {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 0 15px;
            text-align: center;
        }}

        @keyframes slideIn {{
            from {{ transform: translateY(-50px); opacity: 0; }}
            to {{ transform: translateY(0); opacity: 1; }}
        }}

        .header .logo {{
            background-image: url('https://i.ibb.co/gwFSW8B/image.png');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            width: 180px;
            height: 180px;
            margin-right: 15px;
        }}

        .header .text {{
            flex-grow: 1;
            text-align: center;
        }}

        .header h1 {{
            font-size: 30px;
            font-weight: 700;
            letter-spacing: 1px;
            margin: 0;
        }}

        .header p {{
            font-size: 18px;
            color: #6c757d;
            margin: 0;
        }}

        .social-icons {{
            position: relative;
            display: flex;
            justify-content: center;
        }}

        .header .social-icons a {{
            position: relative;
            display: flex;
            justify-content: center;
            color: #2c3e50;
            font-size: 24px;
            transition: color 0.3s, transform 0.3s;
            margin: 0 10px;
        }}

        .header .social-icons a:hover {{
            color: #0077B5;
            transform: scale(1.1);
        }}

        .header .social-icons span {{
            font-size: 16px;
            color: #2c3e50;
            margin-left: 5px;
        }}

        .table thead th {{
            background-color: #91b9dc;
            color: black;
            animation: fadeIn 0.8s ease-in-out;
            vertical-align: middle;
        }}

        .table tbody tr:nth-child(odd) {{
            background-color: #f2f2f2;
            animation: fadeIn 0.8s ease-in-out;
        }}

        .table td, .table th {{
            text-align: center;
            vertical-align: middle;
        }}

        .status {{
            display: inline-block;
            width: 100%;
            padding: 5px 15px;
            border-radius: 25px;
        }}

        .great-job {{
            background-color: #60f48086;
            color: #1f6f31;
        }}

        .havent {{
            background-color: #f5a1a8a8;
            color: #631d24;
        }}

        .table-responsive {{
            border-radius: 15px;
            overflow-x: auto;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            animation: slideIn 0.8s ease-in-out;
        }}

        #searchInput {{
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            margin-top: 10px;
            border: 1px solid rgba(0, 0, 0, 0.326);
            border-radius: 12px;
            animation: slideIn 0.8s ease-in-out;
        }}

        @media (max-width: 768px) {{
            .header .logo {{
                width: 70px;
                height: 70px;
                margin-right: 0; /* Center the logo on smaller screens */
            }}

            .header h1 {{
                font-size: 24px;
            }}

            .header p {{
                font-size: 16px;
            }}

            .header .social-icons a {{
                font-size: 20px;
            }}

            .header .social-icons span {{
                font-size: 14px;
            }}

            .table td, .table th {{
                font-size: 14px;
            }}

            #searchInput {{
                padding: 3px 8px;
                margin-bottom: 5px;
                border-radius: 7px;
                margin-top: 5px;
                font-size: 10px;
            }}
        }}

        @media (max-width: 576px) {{
            .header .logo {{
                width: 60px;
                height: 60px;
                margin-right: 0; /* Center the logo on smaller screens */
            }}

            .header h1 {{
                font-size: 20px;
            }}

            .header p {{
                font-size: 14px;
            }}

            .header .social-icons a {{
                font-size: 14px;
            }}

            .header .social-icons span {{
                font-size: 10px;
            }}

            .table td, .table th {{
                font-size: 12px;
            }}

            #searchInput {{
                padding: 3px 8px;
                margin-bottom: 5px;
                border-radius: 7px;
                margin-top: 5px;
                font-size: 10px;
            }}
        }}

        @media (max-width: 431px) {{
            .header .social-icons a {{
                font-size: 8px;
            }}

            .header .social-icons span {{
                font-size: 7.2px;
                margin-right: 0;
            }}

            .table td, .table th {{
                font-size: 9px;
            }}

            .text h1 {{
                font-size: 13px;
            }}

            .text p {{
                font-size: 10px;
            }}

            .head{{
                margin-bottom: 7px;
            }}

            #searchInput {{
                padding: 3px 8px;
                margin-bottom: 5px;
                border-radius: 7px;
                margin-top: 5px;
                font-size: 10px;
            }}
        }}

        /* Popup Box Styles */
        .popup {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 80%;
            max-width: 500px;
            padding-bottom: 20px;
            background: linear-gradient(135deg, #ffffff, #b7b5b5b8);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            z-index: 1000;
            text-align: center;
            border-radius: 15px;
            display: none;
            animation: popupSlideIn 1s forwards;
        }}

        @keyframes popupSlideIn {{
            from {{ transform: translate(-50%, -60%); opacity: 0; }}
            to {{ transform: translate(-50%, -50%); opacity: 1; }}
        }}

        @keyframes popupSlideOut {{
            from {{ transform: translate(-50%, -50%); opacity: 1; }}
            to {{ transform: translate(-50%, -60%); opacity: 0; }}
        }}

        .popup p {{
            font-size: 16px;
            color: #313131;
            margin-bottom: 20px;
        }}

        .popup p i {{
            font-weight: 550;
        }}

        .popup button {{
            padding: 10px 70px;
            background-color: #73a5d099;
            color: black;
            border: none;
            border-radius: 25px;
            border: 2px solid #344b5f53;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
            cursor: pointer;
            font-size: 18px;
            transition: background-color 0.3s;
        }}

        .popup button:hover {{
            background-color: #a1ccf4;
        }}

        /* Blur background when popup is visible */
        .blur {{
            filter: blur(5px);
            pointer-events: none;
        }}

        .heading {{
            text-align: center;
            padding: 10px 0;
            background: linear-gradient(135deg, #a6cdf457, #91b9dc);
            color: #2c3e50;
            margin-bottom: 20px;
            border-radius: 15px;
        }}

        .heading h2 {{
            margin: 0;
            font-size: 30px;
            font-weight: 700;
            letter-spacing: 1px;
        }}

        @media (max-width: 460px) {{
            .heading h2 {{
                font-size: 20px;
            }}
            .popup p {{
                font-size: 13px;
            }}

            .popup button {{
                padding: 8px 40px;
                font-size: 16px;
            }}
        }}

        .visit-link {{
            padding: 10px 20px;
            background-color: #73a5d099;
            color: black;
            border: none;
            border-radius: 25px;
            border: 1px solid #344b5f53;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
            text-decoration: none;
        }}

        .visit-link:hover {{
            background-color: #a1ccf4;
            color: #000;
            text-decoration: none;
        }}

        .link {{
            margin-top: 20px;
            display: flex;
            justify-content: center;
            flex-direction: column;
            gap: 7px;
        }}

    </style>
</head>
<body>
    <div class="popup" id="popup">
    <div class="heading">
        <h2>⚠️ Important Note:⚠️</h2>
    </div>
        <p>The shown report is <b>till July 30, 12 P.M.</b> I will update it once we receive the latest report from the Arcade Team. <br> <i>Thank you for your patience!</i></p>
        <button onclick="closePopup()">OK</button>
    </div>

    <div class="container" id="content">
        <div class="header">
            <div class="head">
                <div class="logo"></div>
                <div class="text">
                    <h1>Google Cloud Arcade Facilitator</h1>
                    <p>By Team Gourav Sen & Hitansh Sharma</p>
                </div>
                <!--<div class="link">
                    <a href="https://rsvp.withgoogle.com/events/arcade-facilitator/home" class="visit-link" target="_blank"><span>Facilitator Program <i class="ri-gamepad-fill"></i></span></a>
                    <a href="https://go.cloudskillsboost.google/arcade" class="visit-link" target="_blank"><span>Google Arcade <i class="ri-game-fill"></i></span> </a>
                    <a href="https://arcadehelper.vercel.app/pointscalculator" class="visit-link" target="_blank"><span>Points Calculator <i class="ri-calculator-fill"></i></span> </a>
                </div>-->
            </div>
            <div class="social-icons">
                <a href="https://www.linkedin.com/in/gourav61432/" target="_blank"><i class="fab fa-linkedin"></i><span>Gourav Sen</span></a>
                <a href="https://www.linkedin.com/in/hitansh-sharma-b52682234/" target="_blank"><i class="fab fa-linkedin"></i><span>Hitansh Sharma</span></a>
                <a href="https://chat.whatsapp.com/EXBezhYoYLUIscWtDNHJQ4" target="_blank"><i class="fab fa-whatsapp"></i><span>Whatsapp Group</span></a>
                <a href="https://arcadehelper.vercel.app/pointscalculator" target="_blank"><i class="fa-solid fa-calculator"></i><span>Points Calculator </span> </a>
            </div>
        </div>
        <input type="text" id="searchInput" onkeyup="searchTable()" placeholder="Search for names..">
        <div class="table-responsive">
            {html_table}
        </div>
    </div>

    <script>
        // Show the popup when the page loads
        window.onload = function() {{
            document.getElementById("popup").style.display = "block";
            document.getElementById("content").classList.add("blur");
        }};

        // Function to close the popup with animation
        function closePopup() {{
            const popup = document.getElementById("popup");
            popup.style.animation = "popupSlideOut 0.3s forwards";
            setTimeout(() => {{
                popup.style.display = "none";
                document.getElementById("content").classList.remove("blur");
            }}, 200);
        }}

        

        function searchTable() {{
            var input, filter, table, tr, td, i, j, txtValue;
            input = document.getElementById("searchInput");
            filter = input.value.toUpperCase();
            table = document.querySelector(".table");
            tr = table.getElementsByTagName("tr");

            for (i = 1; i < tr.length; i++) {{
                tr[i].style.display = "none"; // Initially hide all rows except the header
                td = tr[i].getElementsByTagName("td");
                for (j = 0; j < td.length; j++) {{
                    if (td[j]) {{
                        txtValue = td[j].textContent || td[j].innerText;
                        if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                            tr[i].style.display = ""; // Show the row if any cell matches the search
                            break; // No need to check other cells in the same row
                        }}
                    }}
                }}
            }}
        }}
    </script>
</body>
</html>
"""

# Write the HTML content to a file with UTF-8 encoding
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
