___

## What I have learnt,
## how I am going to get better at API & SQL.


### SCQA:
___
**Situation**: Sigma course: we are training to be data engineers. Crucially, we are learning about APIs and Databases which will likely be out bread and butter.


**Complication**: I'm doing badly with SQL and not doing well with APIs. My exams are getting worse and I'm not intuiting what needs to be done. I have to constantly look at old notes and modify them to create new work. This means new knowledge is slow to be full ingrained. 


**Question**: How do I get better at SQL and using APIs? What resources do I have to develop those skills and _really_ understand what we have been taught.


__Answer__: I need practice and I have plenty of resources to draw from:
	 1). Cohort didn't complete the API test due to contracted week.
	 2). I was unable to complete the test for backend week 2.
	 3). I was unable to complete the coursework for backend week 2.

I just need to complete the work to date and this will bring me forward. Then I can look for additional learning resources if I need them.

### Current Goal:
___

#### Update:
This weeks' coursework uses the API from last week. So this is a great opportunity to finish last weeks' coursework in the evening so you **can see it all come together** on AWS during the day. Works out well, good opportunity. Put other tasks on back-burner for now.

This week I can creates a link between evening studying and daytime coursework. It's a good opportunity.

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

- You CAN work things out on your own, and without help. But don't bother because you have instructors there specifically to stop you falling behind. Getting behind and catching up works well for you with Python. Don't try for new topics.


### Coach Feedback:
___

- ~~I didn't consider that the `setup-db.sql` file was misconfigured. I thought it would be setup to run correctly as it didn't feel like that was part of the test. It was a personal failing that I overlooked this. However I do think having non-functional files in a test is a bit of an unorthodox move, and it's odd having an 'unreliable narrator' tell you how the test was setup. I think as students, we often feel like the test environment will be a sterile place not a Stanley Parable scenario.~~ This is something I did to myself.

-  ONLY `dicts` are accepted by the tests when checking if the output is correct. Should `RealDictRows` be permissible if the results are the same in postman?

- JSON automatically sorts `dicts`, which I didn't remember and didn't understand. It caused me no end of troubles because it _felt_ like something I should be able to fix. I tried to use an `OrderedDict ` so that `jsonify` didn't change my outputs, but as mentioned above, only `dicts` are allowed. It's probably my fault for missing this for so long but I needed to use `app.json.sort_keys = False`. 

 - I was putting the connection setup and close in each database function. This broke some tests. I feel like I spent a lot of time being confused by this. If this is _a good thing_ in your eyes then great (it _is_ problem solving). Otherwise just be aware it might trip people up. It caught Hamoodi too.

- For the `score_over` condition, the instructions are perhaps unclear. You want us to create averages for experimental scores _across_ species. This wasn't clear to me. Thus I was generating average scores for experiments (with one for each animal) and failing tests.
  
  Note that, in your example, you want the experiment condition to return dates. You cannot average a date, which would be required for this test. At this point I was very stressed so letting me know I could do this in the README would have been nice. I know I should have been able to deduce this.
  
  Maybe being a bit more declarative would be good. Particularly for people like myself who don't intuit the obvious at all well when stressed.

- Also for the `score_over condition`, the instructions state:

 > This parameter should accept only integer values in the range `0`-`100`. When a valid value is passed to the `score_over` parameter, only experiments where the percentage score was **greater than or equal to** the value should be returned.
 
However, unless you use __greater than__ (__not greater than or equal to__) you will fail the final two tests of: `test_api.py::TestExperimentRoute_Task_3::test_returns_expected_data_when_score_is_filtered`


