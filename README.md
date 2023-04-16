# googler
Find anything within your terminal

## Install
```shell
pip install -r requirements.txt
```

Usage:
```shell
google "Facebook"

***** Result 6 *****
Definition in https://en.wikipedia.org/wiki/Facebook
Definition title: Facebook
Facebook is an online social media and social networking service owned by American technology giant Meta Platforms. Created in 2004 by Mark Zuckerberg with fellow Harvard College students and roommates Eduardo Saverin, Andrew McCollum,
 Dustin Moskovitz, and Chris Hughes, its name derives from the face book directories often given to American university students. Membership was initially limited to only Harvard students, gradually expanding to other North American un
iversities and, since 2006, anyone over 13 years old. As of December 2022[update], Facebook claimed 2.96 billion monthly active users,[6] and ranked third worldwide among the most visited websites.[7] It was the most downloaded mobile 
app of the 2010s.[8]
```

```shell
google "Type error: can't compare between a str and an int"

***** Result 1 *****
Solution in https://stackoverflow.com/questions/70867801/why-doesnt-comparing-an-int-to-a-str-raise-a-typeerror
Problem title: Why doesn't comparing an int to a str raise a TypeError?
Number of answer in the discuss: 2

Correct answer:
From the current Python documentation for Comparisons:

Objects of different types, except different numeric types, never compare equal. The == operator is always defined...

(Emphasis mine.)
```



```shell
google "How to iter through a dataloader"

***** Result 0 *****
Solution in https://discuss.pytorch.org/t/iterating-through-a-dataloader-object/25437
Problem title: 
                Iterating through a Dataloader object

Number of answer in the discuss: 4

Correct answer:
The normalization is usually done in the dataset 292 via the transform argument.
The dataloader provides a Python iterator returning tuples and the enumerate will add the step. You can experience this manually (in Python3):
it = iter(train_loader)
first = next(it)
second = next(it)

will give you the first two things from the train_loader that the for loop would get.
Python Iterators are a concept many people ask and write about in various forums, I don’t know a canonical reference to link to, but searching for “python iterators” you’ll find many things on it.
Finally the step, (x, y) works due to “tuple unpacking”, again a general Python thing.
Best regards
Thomas


***** Result 2 *****
Solution in https://stackoverflow.com/questions/69427073/how-to-iterate-over-dataloader-until-a-number-of-samples-is-seen
Problem title: How to iterate over Dataloader until a number of samples is seen?
Number of answer in the discuss: 2

Correct answer:
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

```


