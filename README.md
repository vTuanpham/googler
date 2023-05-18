<p align="center">
  <img src="https://github.com/vTuanpham/googler/assets/82665400/ab905425-ae88-4a40-a3f1-11d8c76810fa" width=27% height=27%> 
  :mag_right:
</p>

### - Find anything quickly within your terminal :computer:
### - Quickly debug your code with provided pre-crawled, correct answer from popular coding disscussion form :sunglasses:

[screen-recorder-wed-may-17-2023-16-11-02.webm](https://github.com/vTuanpham/googler/assets/82665400/a90479b1-7041-407c-a0bc-3a9c2831b58b)


#### Give me a star 🌠 if you find this useful!

## Install

- Have [Node 16.X](https://nodejs.org/es/download/releases) installed.
- Have [Python 3.9](https://www.python.org/downloads/release/python-390/) installed.


```shell
npm install

pip install -r requirements.txt

pyintaller google.spec
```

## Command
```shell
usage: google.exe [-h] [--search_engine SEARCH_ENGINE] [--debug] query

Query result from the internet and returning it back

positional arguments:
  query                 Query string

options:
  -h, --help            show this help message and exit
  --search_engine SEARCH_ENGINE
                        The search engine to query
  --debug               Enable debugging mode and print errors
```

### Usage:

## Image display examples
#### Display current weather condition
<img src="https://user-images.githubusercontent.com/82665400/236262216-eaadb75c-68f0-4fe7-8413-33e415d20bae.PNG"  width=82% height=82%>

#### Display profile of user that have the correct answer
<img src="https://user-images.githubusercontent.com/82665400/236262346-70747901-e975-47cf-8fc5-a5210f4c603f.PNG"  width=82% height=82%>



#### Finding definition
```shell
google "Facebook"

----- |Result| 6 -----
Definition in https://en.wikipedia.org/wiki/Facebook

  Definition title: Facebook

 Definition: 
-----------------
Facebook is an online social media and social networking service owned by American technology giant Meta Platforms. Created in 2004 by Mark Zuckerberg with fellow Harvard College students and roommates Eduardo Saverin, Andrew McCollum,
 Dustin Moskovitz, and Chris Hughes, its name derives from the face book directories often given to American university students. Membership was initially limited to only Harvard students, gradually expanding to other North American un
iversities and, since 2006, anyone over 13 years old. As of December 2022[update], Facebook claimed 2.96 billion monthly active users,[6] and ranked third worldwide among the most visited websites.[7] It was the most downloaded mobile 
app of the 2010s.[8]
-----------------
```
```shell
google "rick roll"

----- |Result| 0 -----
Definition in https://en.wikipedia.org/wiki/Rickrolling

  Definition title: Rickrolling

 Definition: 
-----------------
Rickrolling or a Rickroll is an internet meme involving the unexpected appearance of the music video for the 1987 song "Never Gonna Give You Up", performed by English singer Rick Astley. The aforementioned video has over 1 billion view
s on YouTube. The meme is a type of bait and switch, usually using a disguised hyperlink that leads to the music video. When victims click on a seemingly unrelated link, the site with the music video loads instead of what was expected,
 and they have been "Rickrolled". The meme has also extended to using the song's lyrics, or singing it, in unexpected contexts. Astley himself has also been Rickrolled on several occasions.[1][2][3]
-----------------
```

```shell
google "what is lipstick made out of"

Featured answer: Most lipsticks are made from three basic ingredients: wax, oil, and pigment. Pigment is the color. Waxes provide shape and a spreadable texture. Oils -- such as petrolatum, lanolin, cocoa butter, jojoba, castor, and mi
neral -- add moisture.


----- |Result| 3 -----
Definition in https://en.wikipedia.org/wiki/Lipstick

  Definition title: Lipstick

 Definition:
-----------------
Lipstick is a cosmetic product used to apply coloration and texture to lips, often made of wax and oil. Different pigments are used to produce color, and minerals such as silica may be used to provide texture. The use of lipstick dates
 back to early civilizations such as Sumer and the Indus Valley Civilisation, and was popularized in the Western world in the 16th century. Some lipsticks contain traces of toxic materials, such as lead and PFAS, which prompted health 
concerns and regulation.
-----------------
```

```shell
google "wiki"

Featured answer: A wiki is essentially a database for creating, browsing, and searching through information. A wiki allows non-linear, evolving, complex, and networked text, while also allowing for editor argument, debate, and interact
ion regarding the content and formatting.


----- |Result| 0 -----
Definition in https://en.wikipedia.org/wiki/Wiki#:~:text=A%20wiki%20is%20essentially%20a,regarding%20the%20content%20and%20formatting.

  Definition title: Wiki

 Definition:
-----------------
A wiki (/ˈwɪki/ (listen) WIK-ee) is an online hypertext publication collaboratively edited and managed by its own audience, using a web browser. A typical wiki contains multiple pages for the subjects or scope of the project, and could
 be either open to the public or limited to use within an organization for maintaining its internal knowledge base.
-----------------
```
#### Finding current weather information (readme can't display terminal image :slightly_frowning_face:)
```shell
google "How is the weather in Thu Duc?"

----- |Result| 0 -----
Weather info https://www.accuweather.com/en/vn/thu-duc/414495/weather-forecast/414495

 Weather information: 

 Current weather info on date 4/18: 
-----------------                   
Last update: 11:25 PM
Current temperature: 28°C
Current real feel temperature: RealFeel® 30°C
Current weather description: Mostly clear
-----------------

 Current air quality:
-----------------
Air quality AQI: 25 AQI
Air quality description: Fair
Air quality statement: The air quality is generally acceptable for most individuals. However, sensitive groups may experience minor to moderate symptoms from long-term exposure.
-----------------

 Tomorrow weather info on date 4/19:
-----------------
Tomorrow temperature: 35°/ 27°/ 27°
Tomorrow real feel temperature: RealFeel® 43°
Tomorrow weather description: Clouds and sun
-----------------
```

```shell
google "How is the weather in Bao Loc?"

----- |Result| 0 -----
Weather info https://www.accuweather.com/en/vn/bao-loc/352265/weather-forecast/352265

 Weather information:

 Current weather info on date 4/18:
-----------------
Last update: 11:27 PM
Current temperature: 21°C
Current real feel temperature: RealFeel® 22°C
Current weather description: Partly cloudy
-----------------

 Current air quality:
-----------------
Air quality AQI: 21 AQI
Air quality description: Fair
Air quality statement: The air quality is generally acceptable for most individuals. However, sensitive groups may experience minor to moderate symptoms from long-term exposure.
-----------------

 Tomorrow weather info on date 4/19:
-----------------
Tomorrow temperature: 33°/ 19°/ 19°
Tomorrow real feel temperature: RealFeel® 39°
Tomorrow weather description: Some sun with a stray t-storm
-----------------
```

#### Finding solutions from popular coding discussion forums (readme can't display terminal image :slightly_frowning_face:)

```shell
google "Type error: can't compare between a str and an int"

----- |Result| 1 -----
Solution in https://stackoverflow.com/questions/70867801/why-doesnt-comparing-an-int-to-a-str-raise-a-typeerror

 Problem title: Why doesn't comparing an int to a str raise a TypeError?
 Number of answer in the discuss: 2

 Correct answer:
-----------------
From the current Python documentation for Comparisons:

Objects of different types, except different numeric types, never compare equal. The == operator is always defined...

(Emphasis mine.)
-----------------

```

```shell
google "How to iter through a dataloader"


----- |Result| 0 -----
Solution in https://discuss.pytorch.org/t/iterating-through-a-dataloader-object/25437

 Problem title:
                Iterating through a Dataloader object

 Number of answer in the discuss: 4

 Correct answer:
-----------------
The normalization is usually done in the dataset 293 via the transform argument.
The dataloader provides a Python iterator returning tuples and the enumerate will add the step. You can experience this manually (in Python3):
it = iter(train_loader)
first = next(it)
second = next(it)

will give you the first two things from the train_loader that the for loop would get.
Python Iterators are a concept many people ask and write about in various forums, I don’t know a canonical reference to link to, but searching for “python iterators” you’ll find many things on it.
Finally the step, (x, y) works due to “tuple unpacking”, again a general Python thing.
Best regards
Thomas
-----------------


----- |Result| 2 -----
Solution in https://stackoverflow.com/questions/69427073/how-to-iterate-over-dataloader-until-a-number-of-samples-is-seen

 Problem title: How to iterate over Dataloader until a number of samples is seen?
 Number of answer in the discuss: 2

 Correct answer:
-----------------
You can use torch.utils.data.RandomSampler and sample from your dataset. Here is a minimal setup example:
class DS(Dataset):
    def __len__(self):
        return 5
    def __getitem__(self, index):
        return torch.empty(1).fill_(index)

>>> ds = DS()

Initialize a random sampler providing num_samples and setting replacement to True i.e. the sampler is forced to draw instances multiple times if len(ds) < num_samples:
>>> sampler = RandomSampler(ds, replacement=True, num_samples=10)

Then plug this sampler to a new torch.utils.data.DataLoader:
>>> dl = DataLoader(ds, sampler=sampler, batch_size=2)

>>> for batch in dl:
...     print(batch)
tensor([[6.],
        [4.]])
tensor([[9.],
        [2.]])
tensor([[9.],
        [2.]])
tensor([[6.],
        [2.]])
tensor([[0.],
        [9.]])
-----------------

```


