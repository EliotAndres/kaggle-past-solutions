# Kaggle Past Solutions
A searchable and sortable compilation of [Kaggle](https://www.kaggle.com/) past solutions. [Website](http://ndres.me/kaggle-past-solutions/)

## About
If you are facing a data science problem or just want to learn, there is a good chance that you can find inspiration here !

## Contributing
Many competitions are missing links to their solutions, evaluation and type.

To contribute:
 - Fork the repo
 - Edit the **competitions.json** file (you can even edit it with Github's editor)
 - Make a pull request

For each competition missing the data, please add the following fields:

    "types": [],
    "evaluation": "",
    "solutions": [
      {
        "label": "",
        "url": ""
      }
    ]
Evaluation should contain the name of the evaluation metric and its abreviation (if applicable).
The solutions should be links to the Kaggle forum (if possible) or blog posts.

For instance, you might add:

    "types": ["Image Detection", "Classification"],
    "evaluation": "Multi-class logarithmic loss (logloss)",
    "solutions": [
      {
        "label": "#1 Solution",
        "url": "https://www.kaggle.com/c/state-farm-distracted-driver-detection/forums/t/22906/a-brief-summary"
      },
      {
        "label": "#3 Solution",
        "url": "https://www.kaggle.com/c/state-farm-distracted-driver-detection/forums/t/22631/3-br-power-solution"
      }
    ]
