'''
ITNPBD2 lab sheet. Basic Statistics in Python with Lists
We will store data in a list. This could be for example students’ exam marks. We will now calculate
some basic statistics. Assume list of integers and/or floats. For the start of this exercise, you can
create your own list of students’ marks. We will write a number of Python functions to write the
following functions.
1/ calculate the mean, median and mode of a list of integers and floats.
2/ calculate the deviation of each data point from the mean. The deviation of the ith data point x_i is
the difference between the mean and x_i (i.e. mean – x_i). What is the sum of all of the deviations?
Do you know the answer, and does your code confirm this?
3/ calculate the min and max value. Try and do this without using the built-in min and max functions
already supplied (there are a number of ways to do this). Are the two data points with the min and
max values the ones with the largest deviations? Is this always the case?
4/ calculate the 3 quartiles (see https://en.wikipedia.org/wiki/Quartile). You can test your code as
the 2 nd quartile is just the median. How will you return the 3 numbers?
6/ calculate the number of distinct values in the input list e.g. [1,2,2,3] has 3 distinct values.
7/ compute a list of the distinct values e.g. [1,2,2,3] will give [1,2,3] as the 2 nd 2 is repeated and so is
not distinct.
8/ You thought each item in the list was measured as a percentage in fact it was measures in points
with a range 0 to 50. Write a function which multiples each value by the correct factor (0.5 in this
case), converting it from a percentage (with a range 0 to 100) to a point (with a range 0 to 50).

7/ write a function which returns a “histogram”. You can assume the data is students’ marks (where
values are recorded as percentages ranging from 0 to 100). The bin width for the histogram is 10%,
so the first bin contains the number of students who scored between 0 and 9%. The second bin
contains the number of students who scored between 10% and 19%, and so on.

In the students’ marks case, we have all the data! The statistics we are calculating are descriptive. In
some cases we do not have all the data, and make inferences e.g. we sample the height a subset of
people in the UK and estimate of the mean and standard deviation of the whole population.
The law of large numbers (https://en.wikipedia.org/wiki/Law_of_large_numbers) states as our
sample size get larger our estimate of the mean of the whole population converges (rapidly) to the
true mean. Generate, say 10,000 data points, and take increasing larger sample sizes (with or
without replacement), say 10, 100, 1000 and 10,000. What can you say about the behaviour of other
basic statistics (median, mode, min, max, standard deviation) as the sample size increases? Try this
with uniformly randomly generated data, and also try it for a different distribution of data.
@author: campbell
'''
import random
# Generate list
# ListOfIntegers = [int(random.random()*100.0) for _ in range(0, 50)]
# ListOfFloats = [random.random()*100.0 for _ in range(0, 50)]
# ListOfMarks = ListOfIntegers + ListOfFloats
# print(ListOfMarks)
# print(len(ListOfMarks))
# ListOfMarks.sort()
# print(ListOfMarks)

ListOfMarks = [0, 1, 2, 2, 3.615408513275453, 4.054899187623063, 5, 5, 5.3587978438078725, 5.412402090544022, 6.22554467269082, 7, 8, 8.537214510480373, 8.643165028824118, 10, 11, 11, 12, 13.2618692420575, 13.579914071560506, 13.883506535081757, 14, 14.07701154083487, 14.363643692773753, 15, 15.147075282821454, 15.666231398031517, 16.71828429322083, 18.013994141694447, 18.16942176801558, 19, 22.99906858581253, 23, 24, 24, 24.785523069936666, 27, 28.409295343671882, 29.80456057493932, 29.897499774309054, 30, 33, 34, 35, 38, 39.01422374191784, 39.41636997584853, 40.96544795825413, 41.77584859055735, 42.107471092070156, 43, 44.14918874066264, 44.33140542237628, 44.582287866448524, 47, 50, 55, 58, 59.26312348396278, 60, 62, 62, 62.252930235061676, 64, 64, 64, 64.50081543283378, 65.83807865680298, 67, 69, 70.62870414175904, 74.7346049242652, 74.76437632151651, 76.02928062948638, 76.91834209366223, 77.17303467806343, 78, 78.1336650791283, 78.32397938165506, 78.71527337771958, 83, 83, 86, 86, 86.52543598559, 87.57792531863582, 88, 88, 88.58828235772172, 89, 91, 91, 92, 92.73054422406224, 93.59527689304615, 93.87284078373254, 94, 97.38988407979153]

def ListHistogram(ListOfMarks):
    # assumes list is sorted in ascending order
    BinEnd = 0.09
    BinCount = 0
    Bins = []
    for n in range(10):
        Bins.append(0)
    Count = 0

    for Mark in ListOfMarks:
        Mark = Mark / 100.0
        if Mark <= BinEnd + BinCount/10.0:
            Count +=1
        else:
            Bins[BinCount] = Count
            Count = 1
            BinCount +=1
    Count +=1
    Bins[BinCount] = Count
    print Mark, BinEnd+BinCount/10.0,Count
    return Bins
            
def ListConvert(ListOfMarks):
    ListOfScores = []
    for Mark in ListOfMarks:
        ListOfScores.append(int(Mark*0.5))
    return ListOfScores
                            
def ListMean(ListOfMarks):
    Total = 0.0
    Count = 0
    for Mark in ListOfMarks:
        Total = Total + Mark 
        Count += 1

    return Total / Count

def ListQuartile(ListOfMarks,TypeWanted):
    # always returns float
    if TypeWanted not in ("Median","Lower","Upper"):
        raise Exception
    
    Length = len(ListOfMarks)
    print "Length: ", Length
    Even = Length  % 2 == 0

    if TypeWanted == "Median":
        if Even:
            MidPoint = int(Length/2-0.5)
            Answer = (ListOfMarks[MidPoint] + ListOfMarks[MidPoint + 1])/2.0
        else:
            MidPoint = int(Length/2)
            Answer = ListOfMarks[MidPoint] * 1.0
        
    if TypeWanted == "Lower":
        if Even:            
            LowerList = ListOfMarks[0:int(Length/2)]
            Answer = ListQuartile(LowerList,"Median")
        else: 
            LowerList = ListOfMarks[0:int(Length/2)]
            Answer = ListQuartile(LowerList,"Median")
            
        
    if TypeWanted == "Upper":
        if Even:            
            UpperList = ListOfMarks[int(Length/2):Length]
            Answer = ListQuartile(UpperList,"Median")
        else: 
            UpperList = ListOfMarks[int(Length/2+1):Length]
            Answer = ListQuartile(UpperList,"Median") 
                       
    return Answer

def ListMode(ListOfMarks):
    MaxCountSoFar = 0
    Count = 0
    PossMode = []
    LastMode = 0
    for Mark in ListOfMarks:
        if (Mark) == LastMode: # if current and previous are the same then increment counter
            Count += 1
        else:
            Count = 1
        if Count > MaxCountSoFar: # new contender, adjust measures
            MaxCountSoFar = Count
            PossMode[:] = []    # empties list
            PossMode.append(LastMode)

        elif Count == MaxCountSoFar: # additional contender
            PossMode.append(LastMode)

        LastMode = Mark

    return PossMode

def ListDeviations(ListOfMarks):
    Mean = ListMean(ListOfMarks)
    TotalDev = 0.0
    for Mark in ListOfMarks:
        Dev = Mean - Mark
        TotalDev =TotalDev + Dev
        
    return TotalDev
        
def ListMin(ListOfMarks):
    Min = ListOfMarks[0]   
    for Mark in ListOfMarks:
        if Mark < Min:
            Min = Mark
    return Min

def ListMax(ListOfMarks):
    Max = ListOfMarks[0]   
    for Mark in ListOfMarks:
        if Mark > Max:
            Max = Mark
    return Max    

def ListDistinct(ListOfMarks):
    Distinct = []
    for Mark in ListOfMarks:
        if Mark not in Distinct:
            Distinct.append(Mark)
    return Distinct
    
##################################
#   M A I N                      # 
##################################
print "mean:   ", ListMean(ListOfMarks) 
print "median: ",ListQuartile(ListOfMarks,"Median")
print "lower: ",ListQuartile(ListOfMarks,"Lower")
print "upper: ",ListQuartile(ListOfMarks,"Upper")
print "mode:   ",ListMode(ListOfMarks) 
print "Total deviation: ", ListDeviations(ListOfMarks)
print "Minimum:   ", ListMin(ListOfMarks)  
print "Maximum:   ", ListMax(ListOfMarks)
print "distinct: ", ListDistinct(ListOfMarks)
print "scores: ", ListConvert(ListOfMarks)
print "histogram: ", ListHistogram(ListOfMarks)
                        
                
