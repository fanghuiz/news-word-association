import pandas as pd
import scattertext as st
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import contractions

# URL to download the Data
# http://data.gdeltproject.org/gdeltv3/iatv/ngrams/20190913.KGO.1gram.txt.gz
# http://data.gdeltproject.org/gdeltv3/iatv/ngrams/20190913.KPIX.1gram.txt.gz
# http://data.gdeltproject.org/gdeltv3/iatv/ngrams/20190913.CNN.1gram.txt.gz
# http://data.gdeltproject.org/gdeltv3/iatv/ngrams/20190913.FOXNEWS.1gram.txt.gz
# http://data.gdeltproject.org/gdeltv3/iatv/ngrams/20190913.KNTV.1gram.txt.gz
# http://data.gdeltproject.org/gdeltv3/iatv/ngrams/20190913.MSNBC.1gram.txt.gz


# Import Data
abc_kgo = pd.read_csv("data/20190913/20190913.KGO.1gram.txt",
                      sep="\t",
                      names=["date", "station", "hour", "word", "count"])

cbs_kpix = pd.read_csv("data/20190913/20190913.KPIX.1gram.txt",
                       sep="\t",
                       names=["date", "station", "hour", "word", "count"])

cnn = pd.read_csv("data/20190913/20190913.CNN.1gram.txt",
                  sep="\t",
                  names=["date", "station", "hour", "word", "count"])

fox = pd.read_csv("data/20190913/20190913.FOXNEWS.1gram.txt",
                  sep="\t",
                  names=["date", "station", "hour", "word", "count"])

nbc_kntv = pd.read_csv("data/20190913/20190913.KNTV.1gram.txt",
                       sep="\t",
                       names=["date", "station", "hour", "word", "count"])

msnbc = pd.read_csv("data/20190913/20190913.MSNBC.1gram.txt",
                    sep="\t",
                    names=["date", "station", "hour", "word", "count"])


# Functions to clean data and make plot


def daily_count_clean(df):
    "Get count of word used in a day, with stop words and 1-letter words removed"

    df["word"] = df["word"].astype(str)

    # Keep first element of contraction words, it's = it
    # df["word"] = [word.split("\'")[0].strip() for word in df["word"]]

    # Sum by day
    daily_count = df[["word", "count"]].groupby(["word"]).sum()
    daily_count.reset_index(inplace=True)

    # Expand contraction
    word_clean = [contractions.fix(word) for word in daily_count["word"]]

    # Remove stop words
    word_clean = [word for word in word_clean
                  if word not in ENGLISH_STOP_WORDS]

    # Remove one letter word
    word_clean = [word for word in word_clean if len(word) > 1]

    # Merge with input df, keep only rows with cleaned words
    df_word_clean = pd.DataFrame(word_clean, columns=["word"])
    day_count_clean = pd.merge(daily_count, df_word_clean, on="word")

    return day_count_clean


def stations_merge(station1_df, station1_name,
                   station2_df, station2_name,
                   top_n):
    "Combine station1 and station2, keep top_n number of terms"

    # Merge station1 and station2. Keep all words
    df_merged = pd.merge(station1_df, station2_df,
                         on="word", how="outer").fillna(0)
    df_merged = df_merged.drop_duplicates().set_index("word")
    df_merged.columns = [station1_name, station2_name]

    # Sort and keep top 1000
    df_merged['sum'] = df_merged.iloc[:, 0] + df_merged.iloc[:, 1]
    df_merged = df_merged.sort_values(by="sum", ascending=0)
    df_merged = df_merged.iloc[:top_n].drop(columns="sum")

    return df_merged


def gen_stPlot(df, column_on_y, y_name, x_name, output_file,
               height=None, width=None):
    "Generate scattertext plot and save as local html"

    TCF = st.TermCategoryFrequencies(df)
    plot = st.produce_scattertext_explorer(TCF,
                                           category=column_on_y,
                                           category_name=y_name,
                                           not_category_name=x_name,
                                           show_characteristic=False,
                                           height_in_pixels=height,
                                           width_in_pixels=width)

    open(output_file, 'wb').write(plot.encode('utf-8'))


# Clean and merge data
abc_clean = daily_count_clean(abc_kgo)
cbs_clean = daily_count_clean(cbs_kpix)
cnn_clean = daily_count_clean(cnn)
fox_clean = daily_count_clean(fox)
nbc_clean = daily_count_clean(nbc_kntv)
msnbc_clean = daily_count_clean(msnbc)


# ABC and FOX
abc_fox = stations_merge(abc_clean, "abc", fox_clean, "fox", 1000)

gen_stPlot(df=abc_fox,
           column_on_y="abc",
           y_name="ABC (SF affiliate KGO)",
           x_name="Fox News",
           output_file="plot/abc_fox_20190913.html")


# CBS and FOX
cbs_fox = stations_merge(cbs_clean, "cbs", fox_clean, "fox", 1000)

gen_stPlot(df=cbs_fox,
           column_on_y="cbs",
           y_name="CBS (SF affiliate KPIX) ",
           x_name="Fox News",
           output_file="plot/cbs_fox_20190913.html")


# CNN and FOX
cnn_fox = stations_merge(cnn_clean, "cnn", fox_clean, "fox", 1000)

gen_stPlot(df=cnn_fox,
           column_on_y="cnn",
           y_name="CNN",
           x_name="Fox News",
           output_file="plot/cnn_fox_20190913.html")


# NBC and FOX
nbc_fox = stations_merge(nbc_clean, "nbc", fox_clean, "fox", 1000)

gen_stPlot(df=nbc_fox,
           column_on_y="nbc",
           y_name="NBC (SF affiliate KNTV)",
           x_name="Fox News",
           output_file="plot/nbc_fox_20190913.html")


# MSNBC and FOX
msnbc_fox = stations_merge(msnbc_clean, "msnbc", fox_clean, "fox", 1000)

gen_stPlot(df=msnbc_fox,
           column_on_y="msnbc",
           y_name="MSNBC",
           x_name="Fox News",
           output_file="plot/msnbc_fox_20190913.html")
