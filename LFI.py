from Pre_processing import *

from problog.program import PrologString
from problog.learning import lfi

model = """
1/2::sex.
1/2::classs.
1/2::parch.
1/3::young; 1/3::adult; 1/3::old.
1/3::low; 1/3::average; 1/3::high.

t(_)::status(boy) :- sex, young.
t(_)::status(girl) :- \+sex, young.
t(_)::status(man) :- sex, adult.
t(_)::status(woman) :- \+sex, adult.
t(_)::status(old_man) :- sex, old.
t(_)::status(old_woman) :- \+sex, old.

t(_)::wealth(very_rich) :- classs, high.
t(_)::wealth(rich) :- classs, average.
t(_)::wealth(middle) :- \+classs, average.
t(_)::wealth(poor) :- \+classs, low.

t(_)::survived :- status(X), wealth(Y), parch.
t(_)::survived :- status(X), wealth(Y), \+parch.

"""

example = getExample()
print(len(example))

score, weights, atoms, iteration, lfi_problem = lfi.run_lfi(PrologString(model), example, output_model="trained_model.txt")

print (lfi_problem.get_model())