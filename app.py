from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Pytje pergjigje te paraperacktuara ktu jan dictionary aka hashtables qe kemi ne java 
gym_chatbot_responses = {
    "What are your gym hours?": "Our gym is open from 6 AM to 10 PM every day.",
    "What time does the gym open?": "Our gym opens at 6 AM and closes at 10 PM daily.",
    "Kur eshte hapur palestra?": "Palestra eshte hapur nga ora 6 e mengjesit deri ne 10 te mbremjes cdo dite.",
    
    "Do you offer personal training?": "Yes! We have certified personal trainers available. Please inquire at the front desk for pricing and scheduling.",
    "Is personal training available?": "Yes, our personal trainers are certified and available for booking.",
    "A keni trajner personal?": "Po! Kemi trajner te certifikuar qe mund te rezervoni.",
    
    "What membership plans do you have?": "We offer monthly, quarterly, and yearly membership plans. Prices vary based on the plan and included amenities.",
    "How much does a membership cost?": "Membership prices depend on the duration and included facilities. Contact us for details!",
    "Cilat jane planet e anetaresimit?": "Ne ofrojme plane mujore, tremujore dhe vjetore. Cmimet varen nga shërbimet e perfshira.",
    "Sa kushton?": "Ne ofrojme plane mujore, tremujore dhe vjetore. Cmimet varen nga sherbimet e perfshira.",
    "Sa eshte cmimi?": "Ne ofrojme plane mujore, tremujore dhe vjetore. Cmimet varen nga sherbimet e perfshira.",

    
    "Do you have group classes?": "Yes! We offer yoga, HIIT, and spinning classes throughout the week. Check our class schedule for more details.",
    "What classes do you offer?": "We provide yoga, HIIT, pilates, and Zumba classes.",
    "A keni klasa ne grup?": "Po! Ne ofrojme klasa si joga, HIIT dhe spinning gjate gjithe javes.",
    "A keni grupe?": "Po! Ne ofrojme klasa si joga, HIIT dhe spinning gjate gjithe javes.",
    "A keni individual?": "Po! Ne ofrojme klasa si joga, HIIT dhe spinning gjate gjithe javes me trajner privat.",
    "A keni ne grup?": "Po! Ne ofrojme klasa si joga, HIIT dhe spinning gjate gjithe javes.",
    "A keni trajnim ne grup?": "Po! Ne ofrojme klasa si joga, HIIT dhe spinning gjate gjithe javes.",
    "Cfare klasash keni?": "Ne ofrojme klasa si joga, HIIT dhe spinning gjate gjithe javes.",


    
    "Is there a trial membership available?": "Yes, we offer a 3-day free trial for new members!",
    "Can I try the gym before signing up?": "Yes! We offer a free 3-day trial for new visitors.",
    "A ka anetaresim prove?": "Po, ofrojme nje prove falas per 3 dite per anetaret e rinj!",
    "Cfare ofertash keni?": "Ofrojme nje prove falas per 3 dite per anetaret e rinj!",

    
    "What equipment do you have?": "Our gym is equipped with treadmills, ellipticals, free weights, resistance machines, and more!",
    "What machines are available?": "We have cardio machines, weightlifting equipment, and resistance training machines.",
    "Cfare pajisjesh keni ne palester?": "Palestra jone ka pajisje si rutine, eliptike, pesha te lira dhe makineri rezistence!",
    "Cfare pajisjesh keni?": "Palestra jone ka pajisje si rutine, eliptike, pesha te lira dhe makineri rezistence!",
    "Si jane oraret?": "Kemi orare per kedo pasi palestra jone eshte hapur nga ora 7:00 - 21:00",
    "Ku ndodheni?":"Ne ndodhemi ne komune te parisit para rrethrotullimit."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def chatbot_response():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        
        # Get response or default message
        bot_response = gym_chatbot_responses.get(user_message, "Me falni, nuk ju kuptova.Une i pergjigjem vetem pyetjeve rreth TechnoGym!")

        return jsonify({"response": bot_response})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"response": "An error occurred. Please try again later."})

if __name__ == '__main__':
    app.run(debug=True)