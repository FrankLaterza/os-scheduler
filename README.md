# OS Scheduler
## Introduction
You are tasked with implementing three process scheduling algorithms: FIFO (First In, First Out), Pre-emptive SJF (Shortest Job First), and Round Robin in Python, but using ChatGPT. ChatGPT's implementation should be able to simulate the scheduling of multiple processes under each algorithm and calculate their turnaround time, response time, and wait time.

## Requirements
- [ ] A data structure to represent a process, including its arrival time, execution time, and status.
- [ ] A scheduler function for each algorithm that takes in a list of processes and implements the chosen scheduling algorithm.
- [ ] A time slice parameter (Q-value) for Round Robin, which determines how long each process should be allowed to run before being preempted.
- [ ] A function to calculate our standard metrics: turnaround time, waiting time, and response time for each process.
You will be provided with test inputs and outputs to use as a benchmark for your results.
- [ ] All team members must generate at least one prompt
- [ ] All human-written code must be commented
- [ ] Your script must accept a single command-line parameter for the input filename. i.e.:
scheduler-gpt.py inputFile.in
- [ ] Filename must be the only and required parameter. The input filename should have the extension of ".in".
- [ ] Your script will write out the output file as the base filename with the extension of ".out" i.e.:
inputFile.in should result in an output file called inputFile.out

## Input
### Format
processcount 3  # Read 3 processes
runfor 20       # Run for 20 time units
use sjf
process name A arrival 0 burst 5
process name B arrival 1 burst 4
process name C arrival 4 burst 2
end

### Requirements
- [ ] processcount	Number of processes in the list
- [ ] runfor	How many time ticks to run in total
- [ ] use	The algorithm to use. Valid values: fcfs, sjf, rr
- [ ] quantum	(for rr only) length of the quantum in time ticks
- [ ] process	see below
- [ ] end	end of file marker
- [ ] The process takes three named parameters:
- [ ] name: The name of your process. This can be any valid string.
- [ ] arrival: The arrival time of the process
- [ ] burst: Total burst time

### Error Handling
- [ ] If use specifies 'rr' and there is no quantum specified, print an error message and exit.
- [ ] In general, if any of the required parameters are missing, print an error and exit.
- [ ] Error message should be in the form of:  Error: Missing parameter <parameter>.
- [ ] In the case of missing quantum parameter when use is 'rr' print:  Error: Missing quantum parameter when use is 'rr'
- [ ] If the input file is not provided, Print a usage message:   Usage: scheduler-get.py <input file>

## Output
### Format
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

### Requirements
- [ ] Number of processes
- [ ] The algorithm used
- [ ] When Round Robin is selected, print the Quantum on a separate line immediately following the display of the algorithm used.
- [ ] Every time tick which experiences an event (i.e. processes arrived, selected, and finished)
- [ ] When the CPU is not used, print "Idle"
- [ ] Note the last time tick.
- [ ] In your experimentation, you may have processes that don't complete within the given runtime. List those unfinished processes on the final summary line as P1 did not finish.

## Deliverables
- [X] "Group-N Final Report.docx"
    - [X] Names & Member conversation history links at top
    - [ ] How did we choose which prompts to use?
    - [ ] Rubric for quality of AI code
- [ ] scheduler-gpt.py
    - [ ] Names in comments at the top of file

### AI Code Evaluation
Correctness: Does the code perform the intended task correctly? Are there any bugs or errors that need to be fixed?

Efficiency: Is the code efficient and avoid unnecessary computations or data structures? Can the code be optimized for better performance?

Readability: Is the code well-organized, well-documented, and easy to understand? Does the code follow best practices such as using meaningful variable names, avoiding code duplication, and use a consistent coding style between prompts?

Completeness: Does the code handle edge cases and error conditions appropriately? Is the code flexible enough to handle different input data and scenarios? What happens when you don't feed it an input file or a malformed input file? Does the code account for race conditions (i.e. when two processes can technically be scheduled at the same time)?

Innovation: Does the code offer any new or innovative approaches or ideas for solving the problem at hand? Does the code leverage any new or emerging technologies or frameworks?

Overall Quality and Final Recommendation: Based on the above criteria, how would you rate the overall quality of the code? Would you recommend any changes or improvements to make the code more effective or efficient? How would you rate your overall experience writing code using the assistance of an AI? Was it easier or harder than you expected? What did you learn through the process? What would you do differently if you had to write code via AI again?

### Bonus
Bonus Points (10 points)
Generated Code implements novel features such as:
Enhanced output rendering. This can be through the use of HTML, Markdown, or terminal codes to implement tables, colored text, or even animation.
Other scheduling algorithms like Linux's CFS.
Enhanced interface like a GUI.