{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d9215367",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter in a year: 1700\n",
      "Enter in a month: 1\n",
      "Enter in a day (fractional days allowed): 4\n",
      "The Julian date for this date is: 2341975.5\n"
     ]
    }
   ],
   "source": [
    "from math import trunc\n",
    "\n",
    "Y = int(input(\"Enter in a year: \"))\n",
    "M = int(input(\"Enter in a month: \"))\n",
    "D = float(input(\"Enter in a day (fractional days allowed): \"))\n",
    "\n",
    "JD = 367*Y - 7*trunc((Y+trunc((M+9)/12))/4) - 3*trunc((trunc((Y+trunc((M-9)/7))/100) + 1)/4) + trunc((275*M)/9) + D + 1721029-0.5\n",
    "\n",
    "print(f\"The Julian date for this date is: {JD}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "578ab64d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
