import discord
from discord.ext import commands

# configure bot
TOKEN = "MTI3NTIwMjkxMjU2NTMzNDA0Ng.GqbsEs.OXhRIsQ4N6iYfiDn5M9EweQPzxzgZKwX0j6-yg"
PREFIX = "!"

# create bot instance
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
intents.message_content = True

# sample course data
courses = {
    "ECE212": {
        "name": "Circuit Analysis",
        "description": "Methods for the analysis and design of electrical circuits and systems with an emphasis on the "
                       "frequency domain. AC power system concepts such as real and reactive power, power factor, "
                       "complex power and power flow analysis. For sinusoidal steady-state analysis, topics include "
                       "phasor analysis, impedance and admittance. Review of circuit analysis techniques, differential "
                       "equations and second-order RLC circuits. Frequency domain analysis, including the Laplace "
                       "transform, poles and zeros, s-domain analysis, transfer functions, convolution, frequency "
                       "response, Bode diagrams, frequency response and filter types (e.g. low-pass, high-pass) Circuit "
                       "elements introduced include operational amplifiers, coupled inductors and ideal transformers, "
                       "and the realization of active filters using operational amplifiers.",
        "prerequisites": "None"
    },
    "ECE216": {
        "name": "Signals and Systems",
        "description": "Fundamental discrete- and continuous-time signals, definition and properties of systems, "
                       "linearity and time invariance, convolution, impulse response, differential and difference "
                       "equations, Fourier analysis, sampling and aliasing, applications in communications.",
        "prerequisites": "None"
    },
    "ECE221": {
        "name": "Electricity and Magnetism",
        "description": "The fundamental laws of electromagnetics are covered, including Coulomb's law, Gauss' law, "
                       "Poisson's and Laplace's equations, the Biot-Savart law, Ampere's law, Faraday's law, and "
                       "Maxwell's equations. Vector calculus is applied to determine the relationship between the "
                       "electric and magnetic fields and their sources (charges and currents). The interaction of the "
                       "fields with material media will be discussed, including resistance, polarization in "
                       "dielectrics, magnetization in magnetic materials, properties of magnetic materials and boundary "
                       "conditions. Other topics include: electric and magnetic forces, the electric potential, "
                       "capacitance and inductance, electric and magnetic energy, magnetic circuits, and boundary-value"
                       " problems.",
        "prerequisites": "None"
    },
    "ECE243": {
        "name": "Computer Organization",
        "description": "Basic computer structure. Design of central processing unit. Hardwired control. Input-output "
                       "and the use of interrupts. Assembly language programming. Main memory organization and caches. "
                       "Peripherals and interfacing. System design considerations. The laboratory will consist of "
                       "experiments involving logic systems and microprocessors and a large open project. Design "
                       "activity constitutes a major portion of laboratory work.",
        "prerequisites": "None"
    },
    "ECE297": {
        "name": "Software Design and Organization",
        "description": "An introduction to engineering design processes, illustrated by the design and implementation "
                       "of a software system, and to effective oral and written communication in a team context. "
                       "Principles of software design, project management and team work are developed in the lectures "
                       "and tutorials, and students apply these concepts in the laboratories as they work in a team to "
                       "design and implement a complex software system. Students learn and practice oral and written "
                       "communication techniques in lectures and in meetings with their communication instructor, and "
                       "apply these techniques in a variety of documents and presentations, such as short status "
                       "reports and longer design proposals and design reviews. Students learn software development "
                       "tools such as version control (git), debuggers, code verifiers and unit test frameworks and "
                       "gain experience in graphical user interface design and algorithm development.",
        "prerequisites": "APS105, ECE244"
    }
}

@bot.command()
async def c(ctx, code: str):
    code = code.upper()
    if code in courses:
        course_info = courses[code]
        embed = discord.Embed(title=f"{code}: {course_info['name']}", color=0x3498db)
        embed.add_field(name="Description", value=course_info["description"], inline=False)
        embed.add_field(name="Prerequisites", value=course_info["prerequisites"], inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Course `{code}` not found.")


# run the bot
bot.run(TOKEN)