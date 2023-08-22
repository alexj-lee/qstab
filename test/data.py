import pytest
import json


@pytest.fixture
def load_test_seq():
    with open("./test/data.json", "r") as f:
        # json with:
        """
        "question": "A 40-year-old zookeeper presents to the emergency department
        complaining of severe abdominal pain that radiates to her back, and nausea.
        The pain started 2 days ago and slowly increased until she could not tolerate
         it any longer. Past medical history is significant for hypertension and
         hypothyroidism. Additionally, she reports that she was recently stung by
         one of the zoo\u2019s smaller scorpions, but did not seek medical treatment.
        She takes aspirin, levothyroxine, oral contraceptive pills, and a
        multivitamin daily. Family history is noncontributory. Today, her blood
        pressure is 108/58 mm Hg, heart rate is 99/min, respiratory rate is 21/min,
        and temperature is 37.0\u00b0C (98.6\u00b0F). On physical exam, she is a
        well-developed, obese female that looks unwell. Her heart has a regular rate
        and rhythm. Radial pulses are weak but symmetric. Her lungs are clear to
        auscultation bilaterally. Her lateral left ankle is swollen, erythematous,
        and painful to palpate. An abdominal CT is consistent with acute pancreatitis.
         Which of the following is the most likely etiology for this patient\u2019s
         disease?", "answer": "Scorpion sting", "options":
         {"A": "Aspirin", "B": "Oral contraceptive pills", "C": "Scorpion sting", "D": "Hypothyroidism", "E": "Obesity"},
        "meta_info": "step1", "answer_idx": "C"}
        """

        return json.load(f)
