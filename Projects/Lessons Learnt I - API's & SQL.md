___

## What I have learnt,
## how I am going to get better at API & SQL.


### SCQA:
___
**Situation**: Sigma course, we are training to be data engineers. Crucially, we are learning about APIs and Databases which will likely be out bread and butter.


**Complication**: I'm doing badly with SQL and not doing well with APIs. My exams are getting worse and I'm not intuiting what needs to be done, I have to constantly look at old notes and modify them to create new work.


**Question**: How do I get better at SQL and using APIs? What resources do I have to develop those skills?


__Answer__: I need practice and I have plenty of resources to draw from:
	 1). ~~API's test one was never completed (Bank Holiday contracted the week)~~ - Website offline.
	 2). I was unable to complete the test for backend week 2.
	 3). I was unable to complete the coursework for backend week 2.

I just need to complete the work to date and this will bring me forward. Then I can look for additional learning resources.

### Current Goal:
___

__High Priority:__
- [ ] Pass two tests from the Backend week 2 assessment each evening until complete.
- [ ] Pass the API test from Backend week 1.

__Low Priority__
- [ ] Return to the coursework - would you still benefit from completing it?
 
__Consider__:
 We have been given access to AWS. Is there anything simple you can do that would utilise this service in your free time?


### Lessons Learnt:
___

- When dealing with multiple tables and SQL, take time to really homogenise the naming schemes. It is VERY hard to debug when names are very similar but not quite the same.

 - Making a more aggressive push through the coursework on the Monday will make subsequent workshops make a lot more sense, as you will be dealing with the problem they are discussing.


### Coach Feedback:
___

- I didn't consider that the `setup-db.sql` file was misconfigured. I thought it would be setup to run correctly as it didn't feel like that was part of the test. It was a personal failing that I overlooked this. However I do think having non-functional files in a test is a bit of an unorthodox move, and it's odd having an 'unreliable narrator' tell you how the test was setup. I think as students, we often feel like the test environment will be a sterile place not a Stanley Parable scenario.

 - I was putting the connection setup and close in each database function. This broke some tests. I feel like I spent a lot of time being confused by this. If this is _a good thing_ in your eyes then great. I feel like maybe it highlighted a flaw in my understanding of testing, not SQL and APIs.

- For the `score_over` condition, the instructions are unclear. I think you want us to create averages for experimental scores _across_ species. You do not state this anywhere. Thus generating average scores for experiments (with one for each animal) will fail tests. 
  
  However in your example you want the experiment condition to return dates. You cannot average a date, which would be required for this test.