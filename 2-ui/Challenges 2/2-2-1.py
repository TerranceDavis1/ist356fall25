{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb09c285",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "positional argument follows keyword argument (1111196630.py, line 3)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31m@interact_manual (names= '' , major = [IST, ADA, IMT], gpa = 0.0, 4.0, 0.05 )\u001b[39m\n                                                                                ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m positional argument follows keyword argument\n"
     ]
    }
   ],
   "source": [
    "from ipywidgets import interact_manual\n",
    "from IPython.display import display\n",
    "@interact_manual (names= '' , major = (IST, ADA, IMT), gpa =(0.0, 4.0, 0.05))\n",
    "\n",
    "def onclick(names,major,gpa):\n",
    "    if gpa < 1.8:\n",
    "        status = \"probation\"\n",
    "    elif gpa > 3.4:\n",
    "        status = \"deans list\"\n",
    "    else:\n",
    "        status = \"no list\"\n",
    "    display (f\"{names},{gpa},{major}, {status}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
