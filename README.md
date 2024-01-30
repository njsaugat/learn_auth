**When migrations don't work remove all the migrations**
```
find . -path "_/migrations/_.py" -not -name "**init**.py" -delete
```

