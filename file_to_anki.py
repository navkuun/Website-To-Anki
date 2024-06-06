import enum
from pydantic import BaseModel, Field
from openai import OpenAI
import instructor
from typing import List

# Apply the patch to the OpenAI client
# enables response_model keyword
client = instructor.from_openai(OpenAI())


class Flashcard(BaseModel):
    """
    Class for anki flashcard question and content
    """

    question: str
    content: str = Field(
        description="The content of the flashcard, first explain the concept as if you were talking to a sixth grader then go into more technical detail"
    )


def createFlashcards(data: str) -> List[Flashcard]:
    """Perform single-label classification on the input text."""
    return client.chat.completions.create(
        model="gpt-4o",
        response_model=List[Flashcard],
        messages=[
            {
                "role": "user",
                "content": f"""
Your task is to take some text and turn it into a series of flashcards relevant to the topic.

Each flashcard must have a question and content field.

The flashcards must have the question enclosed in a h2 tag and the content inside a h3 tag along with qutotations.

Here is the text:

{data}

---
Here are some examples:
"<h2 class=""card-question-text"" itemprop=""name text""> variable </h2> "	"<h3 class=""card-answer-text"" itemprop=""text""> named locations that store data in which the contents can be changed during program execution </h3>"

"<h2 class=""card-question-text"" itemprop=""name text""> local variable </h2> "	"<h3 class=""card-answer-text"" itemprop=""text""> declared inside a function. They can only be accessed and used in that function. </h3>"

"<h2 class=""card-question-text"" itemprop=""name text""> global variable </h2> "	"<h3 class=""card-answer-text"" itemprop=""text""> declared outside of all the functions, they can be used throughout the whole program including inside functions. </h3>"

"<h2 class=""card-question-text"" itemprop=""name text""> advantages of functions </h2> "	"<h3 class=""card-answer-text"" itemprop=""text""> easier to create and test </h3>"

"<h2 class=""card-question-text"" itemprop=""name text""> subprogram </h2> "	"<h3 class=""card-answer-text"" itemprop=""text""> self-contained units of code that perform some well-defined purpose. </h3>"

"<h2 class=""card-question-text"" itemprop=""name text""> function </h2> "	"<h3 class=""card-answer-text"" itemprop=""text""> a subprogram that ALWAYS returns a single value </h3>"

"<h2 class=""card-question-text"" itemprop=""name text""> procedure </h2> "	"<h3 class=""card-answer-text"" itemprop=""text""> a subprogram that returns one or many values. </h3>"
---
You must ensure that each flashcard created is to explain a concept, do not focus on history.
Think this through this step by step.
""",
            },
        ],
    )


example_text = """
The light that we see everyday is only a fraction of the total energy emitted by the sun incident on the earth. Sunlight is a form of "electromagnetic radiation" and the visible light that we see is a small subset of the electromagnetic spectrum shown at the right.

The electromagnetic spectrum describes light as a wave which has a particular wavelength. The description of light as a wave first gained acceptance in the early 1800's when experiments by Thomas Young, François Arago, and Augustin Jean Fresnel showed interference effects in light beams, indicating that light is made of waves. By the late 1860's light was viewed as part of the electromagnetic spectrum. However, in the late 1800's a problem with the wave-based view of light became apparent when experiments measuring the spectrum of wavelengths from heated objects could not be explained using the wave-based equations of light. This discrepancy was resolved by the works of 1 in 1900, and 2 in 1905. Planck proposed that the total energy of light is made up of indistinguishable energy elements, or a quanta of energy. Einstein, while examining the photoelectric effect (the release of electrons from certain metals and semiconductors when struck by light), correctly distinguished the values of these quantum energy elements. For their work in this area Planck and Einstein won the Nobel prize for physics in 1918 and 1921, respectively and based on this work, light may be viewed as consisting of "packets" or particles of energy, called photons..

Today, quantum-mechanics explains both the observations of the wave nature and the particle nature of light. In quantum mechanics, a photon, like all other quantum-mechanical particles such as electrons, protons etc, is most accurately pictured as a "wave-packet". A wave packet is defined as a collection of waves which may interact in such a way that the wave-packet may either appear spatially localized (in a similar fashion as a square wave which results from the addition of an infinite number of sine waves), or may alternately appear simply as a wave. In the cases where the wave-packet is spatially localized, it acts as a particle. Therefore, depending on the situation, a photon may appear as either a wave or as a particle and this concept is called "wave-particle duality".

A complete physical description of the properties of light requires a quantum-mechanical analysis of light, since light is a type of quantum-mechanical particle called a photon. For photovoltaic applications, this level of detail is seldom required and therefore only a few sentences on the quantum nature of light are given here. However, in some situations (fortunately, rarely encountered in PV systems), light may behave in a manner which seems to defy common sense, based on the simple explanations given here. The term "common sense" refers to our own observations and cannot be relied on to observe the quantum-mechanical effects because these occur under conditions outside the range of human observation. For further information on the modern interpretation of light please refer to 3. A wave-packet, or photon is pictured as used in PVCDROM below.
"""

output = createFlashcards(data=example_text)

# Write to a text file in Anki format
with open("flashcards.txt", "w", encoding="utf-8") as file:
    for card in output:
        file.write(f"{card.question}\t{card.content}\n")
        print(f"{card.question}\t{card.content}\n")

print("The flashcards have been saved in Anki format.")
