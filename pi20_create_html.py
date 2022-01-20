# define questions
questions = [
       'My face recognition ability is worse than most people',
       'I have always had a bad memory for faces',
       'I find it notably easier to recognize people who have distinctive facial features',
       'I often mistake people I have met before for strangers',
       'When I was at school I struggled to recognize my classmates',
       'When people change their hairstyle, or wear hats, I have problems recognizing them',
       'I sometimes have to warn new people I meet that I am ‘bad with faces’',
       'I find it easy to picture individual faces in my mind',
       'I am better than most people at putting a ‘name to a face’',
       "Without hearing people's voices, I struggle to recognize them",
       'Anxiety about face recognition has led me to avoid certain social or professional situations',
       'I have to try harder than other people to memorize faces',
       'I am very confident in my ability to recognize myself in photographs',
       'I sometimes find movies hard to follow because of difficulties recognizing characters',
       'My friends and family think I have bad face recognition or bad face memory',
       'I feel like I frequently offend people by not recognizing who they are',
       'It is easy for me to recognize individuals in situations that require people to wear similar clothes (e.g. suits, uniforms and swimwear)',
       'At family gatherings, I sometimes confuse individual family members',
       'I find it easy to recognize celebrities in ‘before-they-were-famous’ photos, even if they have changed considerably',
       'It is hard to recognize familiar people when I meet them out of context (e.g. meeting a work colleague unexpectedly while shopping)']

# define which have reversed scoring
reversed_q = [8, 9, 13, 17, 19]

# define header
form = """
<!DOCTYPE html>
<html lang="en">
<header> <h1 style="text-align: center">Introduction to Questionnaire</h1>
<div style="text-align: center">
<p>In this questionnaire we would like to ask you to answer the following 20 short questions. In each there will be a scale from <b>1</b> (strongly <b>disagree</b>) to <b>5</b> (strongly <b>agree</b>). Please answer all questions. </p>
</div>
</header>
<hr>
<body>
<main>
<form>
"""

for i, question in enumerate(questions):
    # if the question has reversed grading
    if i+1 in reversed_q: # account for python numbering
        form += f"""
            <h2 style="text-align: center">Q{i+1}: {question}.</h2>

        <!-- reverse scored (strongly agree is scored ‘1’ and strongly disagree is scored ‘5’) -->
           <div style="text-align: left; position:relative; left:45%">
            <table class="table-plain">
                <input type="radio" value="1" name="q{i+1}" id="q{i+1}_5agree" required> 
                <label for="q{i+1}_5agree"> Strongly agree </label><br>

                <input type="radio" value="2" name="q{i+1}" id="q{i+1}_4agree"> 
                <label for="q{i+1}_4agree"> Moderately agree </label><br>

                <input type="radio" value="3" name="q{i+1}" id="q{i+1}_3neutral"> 
                <label for="q{i+1}_3neutral"> Neutral  </label><br>

                <input type="radio" value="4" name="q{i+1}" id="q{i+1}_2disagree" >
                <label for="q{i+1}_2disagree"> Moderately disagree  </label><br>

                <input type="radio" value="5" name="q{i+1}" id="q{i+1}_1disagree" >
                <label for="q{i+1}_1disagree"> Strongly disagree </label><br>

            </table>  
           </div>
        """
    else:
        form += f"""
            <h2 style="text-align: center">Q{i+1}: {question}.</h2>

       <div style="text-align: left; position:relative; left:45%">
        <table class="table-plain">
            <input type="radio" value="5" name="q{i+1}" id="q{i+1}_5agree" required> 
            <label for="q{i+1}_5agree"> Strongly agree </label><br>

            <input type="radio" value="4" name="q{i+1}" id="q{i+1}_4agree"> 
            <label for="q{i+1}_4agree"> Moderately agree </label><br>

            <input type="radio" value="3" name="q{i+1}" id="q{i+1}_3neutral">
            <label for="q{i+1}_3neutral"> Neutral  </label><br>

            <input type="radio" value="2" name="q{i+1}" id="q{i+1}_2disagree" > 
            <label for="q{i+1}_2disagree"> Moderately disagree  </label><br>

            <input type="radio" value="1" name="q{i+1}" id="q{i+1}_1disagree" > 
            <label for="q{i+1}_1disagree"> Strongly disagree </label><br>

        </table>  
       </div>

        <p> </p>
        """

form += '<hr>\n<input style="display: block; margin:auto" type="submit" value="Submit">\n  </form></main></body>'

# save file
with open("pi20.html", "w") as f:
    f.write(form)