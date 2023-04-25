import justpy as jp


class Doc:

    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')

        jp.Div(a=div, text='Instant Dictionary API', classes='text-4xl m-2')
        jp.Div(a=div, text='Get definitions of words:', classes='text-lg')
        jp.Hr(a=div)
        jp.Div(a=div, text='www.example.com/api?w=moon')
        jp.Hr(a=div)
        jp.Div(a=div, text="""{"word": "Moon", "definition": ["\"The celestial orb which revolves round the earth; 
        the satellite of the earth; a secondary planet whose light borrowed from the sun is reflected to the earth 
        and serves to dispel the darkness of night. The diameter of the moon is 2 160 miles its mean distance from 
        the earth is 240 000 miles and its mass is one eightieth that of the earth. See Lunar month under Month.\"", 
        "\"A secondary planet or satellite revolving about any member of the solar system; as the moons of Jupiter or 
        Saturn.\"", "\"The time occupied by the moon in making one revolution in her orbit; a month.\"", 
        "\"A crescentlike outwork. See Half-moon.\"", "\"To expose to the rays of the moon.\"", "\"To act if 
            moonstruck; to wander or gaze about in an abstracted manner.\""]}""")

        return wp


