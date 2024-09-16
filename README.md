# os-scheduler
Introduction
You are tasked with implementing three process scheduling algorithms: FIFO (First In, First Out), Pre-emptive SJF (Shortest Job First), and Round Robin in Python, but using ChatGPT. ChatGPT's implementation should be able to simulate the scheduling of multiple processes under each algorithm and calculate their turnaround time, response time, and wait time.

ChatGPT's implementation should include the following components:

A data structure to represent a process, including its arrival time, execution time, and status.
A scheduler function for each algorithm that takes in a list of processes and implements the chosen scheduling algorithm.
A time slice parameter (Q-value) for Round Robin, which determines how long each process should be allowed to run before being preempted.
A function to calculate our standard metrics: turnaround time, waiting time, and response time for each process.
You will be provided with test inputs and outputs to use as a benchmark for your results.

Each member of your team will be responsible for providing at least one prompt. You are allowed multiple iterations. You may continue to refine your prompt as much as necessary in order to get desirable results. You are encouraged to compare prompts as a team to arrive at a "best solution" for final submission. However, you will be required to keep and track your prompt history (see below).

At some point, it may seem like continuing prompt iteration yields diminishing returns. At your discretion, you may choose to stop prompting and complete the project on your own. Ideally, human-written code would be limited to output formatting and other superficial, minor tweaks. However, there may be some features or aspects of the project which perhaps ChatGPT refuses to generate. These should be clearly documented. All cases of human-generated code should be commented as such.

Finally, as a caution -- ChatGPT, at least as implemented at OpenAI.com, will occasionally refuse to generate code literally telling you that it can't. You can rephrase your prompt or even just ask it to carry it out regardless ("You've done this before. Please do it now").

Input File Format
Example:

processcount 3  # Read 3 processes
runfor 20       # Run for 20 time units
use sjf
process name A arrival 0 burst 5
process name B arrival 1 burst 4
process name C arrival 4 burst 2
end
directive	definition
processcount	Number of processes in the list
runfor	How many time ticks to run in total
use	The algorithm to use. Valid values: fcfs, sjf, rr
quantum	(for rr only) length of the quantum in time ticks
process	see below
end	end of file marker
The process takes three named parameters:
name: The name of your process. This can be any valid string.
arrival: The arrival time of the process
burst: Total burst time

Remember to check the validity of the use and quantum parameters:

If use specifies 'rr' and there is no quantum specified, print an error message and exit.
In general, if any of the required parameters are missing, print an error and exit.
Error message should be in the form of:  Error: Missing parameter <parameter>.
In the case of missing quantum parameter when use is 'rr' print:  Error: Missing quantum parameter when use is 'rr'
If the input file is not provided:
Print a usage message:   Usage: scheduler-get.py <input file>
Output File Format
Example:

3 processes
Using preemptive Shortest Job First
Time   0 : A arrived
Time   0 : A selected (burst   5)
Time   1 : B arrived
Time   4 : C arrived
Time   5 : A finished
Time   5 : C selected (burst   2)
Time   7 : C finished
Time   7 : B selected (burst   4)
Time  11 : B finished
Time  11 : Idle
Time  12 : Idle
Time  13 : Idle
Time  14 : Idle
Time  15 : Idle
Time  16 : Idle
Time  17 : Idle
Time  18 : Idle
Time  19 : Idle
Finished at time  20

A wait   0 turnaround   5  response 0
B wait   6 turnaround  10  response 6
C wait   1 turnaround   3 response 1
Output must include all of the following:

Number of processes
The algorithm used
When Round Robin is selected, print the Quantum on a separate line immediately following the display of the algorithm used.
Every time tick which experiences an event (i.e. processes arrived, selected, and finished)
When the CPU is not used, print "Idle"
Note the last time tick.
In your experimentation, you may have processes that don't complete within the given runtime. List those unfinished processes on the final summary line as
P1 did not finish
The sample output shows all numerical outputs neatly right-justified. You do not need to do so. Whitespace between elements will suffice without fancy alignment. i.e.:

Time  1
Time  10
Handling input and output
Input
Your script must accept a single command-line parameter for the input filename. i.e.:
scheduler-gpt.py inputFile.in

Filename must be the only and required parameter. The input filename should have the extension of ".in".

Output
Your script will write out the output file as the base filename with the extension of ".out" i.e.:
inputFile.in should result in an output file called inputFile.out