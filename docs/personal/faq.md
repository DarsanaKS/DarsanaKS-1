<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>FAQs</title>
<style>
    .highlight {
        background-color: yellow;
        }
    .current {
        background-color: orange;
    }
/* Customize background color for the question section */
details  {
      /*background-color: #f5f1f1;  Use your preferred color value */
      padding: 10px;
    }
    /* Customize the 3D box effect for the summary section */
    details summary {
      background-color: #17a1a1; 
      padding: 5px 10px;
      border: 1px solid #17b1b1;
      border-radius: 8px;
      box-shadow: 2px 2px 4px rgba(0, 0, 0, 1.4);
      cursor: pointer;
      padding-left: 0;
      text-align: left;
      /*font-size: 14px;
      font-family: Verdana, Geneva, Tahoma, sans-serif;*/
    }
    /* Customize background color for the answer section */
    details p {
      /* background-color: #17a1a1; Use your preferred color value 
      border: 1px solid #17a1a1; */
      padding: 10px;
      margin: 0; /* Remove any default margin to avoid extra spacing */
      /*font-size: 14px;
      font-family: Verdana, Geneva, Tahoma, sans-serif;*/
      line-height: 1.5;
      text-align: left;
      padding-left: 0;
      margin-left: 0;
        }
    p {
        line-height: 1.5; /* Adjust the value to set the desired line height */
        /*font-size: 14px;
        font-family: Verdana, Geneva, Tahoma, sans-serif;*/
    }
    body {
      margin: 0;
      /*background-color: #f5f1f1; Use your preferred color value */
          }
      h1 {
            color: #17a1a1;
            font-size: 35px;
            /*font-family:'Cambria', Times, serif;*/
            text-align: center;
        }
    h2 {
            font-size: 20px;
            /*font-family:'Cambria', Times, serif;*/
            text-align: Center;
        }
    label {
        /*font-weight: bold;
        font-family: 'Cambria', Times, serif;
        font-size: 18px;*/
    }
    
    
 </style>
</head>
<body>
    <div id="content">
            <h1>FREQUENTLY ASKED QUESTIONS</h1>
            <h2>Hello There!<h2>
            <p>Here are some questions you might want to ask.</p>
            <br>
            <details onclick="toggleAccordion(this)">
            <summary>Can you tell me about yourself?</summary>
            <p>I am Darsana, a versatile and adaptable person who always adapts to situation and tries to stay positive.<br>I come from Bangalore, a city in India.<br>
            -----<br>
            I completed education in Kerala, a state in India.  I hold Master's degree in Mathematics and Post Graduate Diploma in Computer Applications.<br>
            After completing my studies, I moved to Bangalore city for career opportunities and growth.<br>
            ------<br>
            I started my career as a technical editor and proof reader where I worked on scientific journals and thesis reports. After 5+ years as a technical editor, I took a maternity and child care break.<br>
            After the break, I had a strong will to upgrade my career goals and started grooming up myself for technical writing. Later on, I got into technical writing and from then I am a enthusiastic technical writer always trying to upgrade myself in different aspects of writing and contributing to the product.
            </p>
            </details>
            <details onclick="toggleAccordion(this)">
            <summary>How long did you take a career break and why?</summary>
            <p>I took a career break of almost 3 years for maternity and child care.<br>
            Two years I was completely on a break, however, third year I started to work partially as an editor.</p>
            </details>
            <details onclick="toggleAccordion(this)">
            <summary>Why do you want to move to Europe?</summary>
            <p>I came to Hungary through a family reunification visa. I started liking the people culture and the development seen in Europe.<br>
            I travelled to places and I felt that I should be part of this lifestyle. <br>
            -----<br>
            I explored the jobs market here and I was really excited to see that technical writer position is a valued position in European IT sector. As I always wanted to enhance and take my career to new levels, I thought to explore the opportunities.</p>
            </details>
            <details onclick="toggleAccordion(this)">
            <summary>Are you looking for a long-term or contract based jobs?</summary>
            <p>I am looking for a long-term/permanant environment where I can contribute to the organization and grow along with it.</p>
            </details>
            <details onclick="toggleAccordion(this)">
            <summary>Do you need work visa in the country applied for?</summary>
            <p>I am a citizen of India. Outside India, I need work sponsorship so that I can apply for work visa.</p>
            </details>
            <details onclick="toggleAccordion(this)">
            <summary>What are your positives and negatives?</summary>
            <p><b>Positives:</b><br>
            I always try to mingle with people and this helped me a lot in my profession.<br>
            I am a person who is happy for small things and try to enjoy life and travel.<br>
            I am good at multi-tasking in my own way. Being a mother taught me a lot of it.<br>
            <b>Negatives:</b><br> I like to talk a lot. However, this has helped my in my profession.<br> 
            </p>
            </details>
            <details onclick="toggleAccordion(this)">
            <summary>What are your thoughts on balancing work and family?</summary>
            <p>Work and family are important at the same time. It is all about co-operation, support, and understanding.<br>
            At times we may have to implement strategies to be success in both.<br>
            A lot of people manage work and family effectively and I believe that is a skill that need to be polished and restructured time to time.</p>
            </details>
            <details onclick="toggleAccordion(this)">
            <summary>What do you want to convey to the reader?</summary>
            <p>I believe in continuous learning and growth; let it be personally or professionaly. Hence I am prepared to takeup any career challenges for my career or upgrade myself to adhere to the requirement and environment.<br>
            Being positive is my strength.</p>
            </details>
            <!-- 
            <details onclick="toggleAccordion(this)">
            <summary></summary>
            <p></p>
            </details>
             -->
            </main>
    </div>
  <script> // JavaScript to handle accordion behavior
    function toggleAccordion(accordion) {
        var detailsElements = document.getElementsByTagName("details");
        for (var i = 0; i < detailsElements.length; i++) {
            if (detailsElements[i] !== accordion) {
                detailsElements[i].removeAttribute("open");
            }
        }
    }
</script>
</body>
</html>