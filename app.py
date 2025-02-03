import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):

        # Stats Area
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user,df)
        # st.title("Top Statistics")
        # st.markdown(
        #     """
        #     <style>
        #     @keyframes blink {
        #         0% { color: red; text-shadow: 0 0 5px red; }
        #         50% { color: white; text-shadow: 0 0 10px red; }
        #         100% { color: red; text-shadow: 0 0 5px red; }
        #     }
        #     .blinking-text {
        #         font-size: 32px;
        #         font-weight: bold;
        #         animation: blink 1s infinite;
        #     }
        #     </style>
        #     <h1 class="blinking-text">Top Statistics</h1>
        #     """,
        #     unsafe_allow_html=True
        # )

        # Add glowing, jumping, and red effect using HTML & CSS
        # st.markdown(
        #     """
        #     <style>
        #     @keyframes glow {
        #         0% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
        #         50% { text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red; transform: translateY(-5px); }
        #         100% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
        #     }
        #     .glowing-text {
        #         font-size: 40px;
        #         font-weight: bold;
        #         color: white;
        #         text-align: center;
        #         animation: glow 1s infinite alternate;
        #     }
        #     </style>
        #     <h1 class="glowing-text">Top Statistics</h1>
        #     """,
        #     unsafe_allow_html=True
        # )

        st.markdown(
            """
            <style>
            @keyframes glow {
                0% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
                50% { text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red; transform: translateY(-5px); }
                100% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
            }
            .glowing-text {
                font-size: 40px;
                font-weight: bold;
                color: white;
                text-align: left;  /* Align to the left */
                animation: glow 1s infinite alternate;
            }
            </style>
            <h1 class="glowing-text">Top Statistics</h1>
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        # monthly timeline
        st.markdown(
            """
            <style>
            @keyframes glow {
                0% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
                50% { text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red; transform: translateY(-5px); }
                100% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
            }
            .glowing-text {
                font-size: 40px;
                font-weight: bold;
                color: white;
                text-align: left;  /* Align to the left */
                animation: glow 1s infinite alternate;
            }
            </style>
            <h1 class="glowing-text">Monthly Timeline</h1>
            """,
            unsafe_allow_html=True
        )
        # st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        st.markdown(
            """
            <style>
            @keyframes glow {
                0% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
                50% { text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red; transform: translateY(-5px); }
                100% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
            }
            .glowing-text {
                font-size: 40px;
                font-weight: bold;
                color: white;
                text-align: left;  /* Align to the left */
                animation: glow 1s infinite alternate;
            }
            </style>
            <h1 class="glowing-text">Daily Timeline</h1>
            """,
            unsafe_allow_html=True
        )
        # st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # activity map
        st.markdown(
            """
            <style>
            @keyframes glow {
                0% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
                50% { text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red; transform: translateY(-5px); }
                100% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
            }
            .glowing-text {
                font-size: 40px;
                font-weight: bold;
                color: white;
                text-align: left;  /* Align to the left */
                animation: glow 1s infinite alternate;
            }
            </style>
            <h1 class="glowing-text">Activity Map</h1>
            """,
            unsafe_allow_html=True
        )
        # st.title('Activity Map')
        col1,col2 = st.columns(2)

        with col1:
            st.markdown(
                """
                <style>
                @keyframes glow {
                    0% { text-shadow: 0 0 5px blue, 0 0 10px blue, 0 0 15px blue; transform: translateY(0px); }
                    50% { text-shadow: 0 0 10px blue, 0 0 20px blue, 0 0 30px blue; transform: translateY(-5px); }
                    100% { text-shadow: 0 0 5px blue, 0 0 10px blue, 0 0 15px blue; transform: translateY(0px); }
                }
                .glowing-text {
                    font-size: 40px;
                    font-weight: bold;
                    color: white;
                    text-align: left;  /* Align to the left */
                    animation: glow 1s infinite alternate;
                }
                </style>
                <h1 class="glowing-text">Most busy day</h1>
                """,
                unsafe_allow_html=True
            )

            # st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.markdown(
                """
                <style>
                @keyframes glow {
                    0% { text-shadow: 0 0 5px blue, 0 0 10px blue, 0 0 15px blue; transform: translateY(0px); }
                    50% { text-shadow: 0 0 10px blue, 0 0 20px blue, 0 0 30px blue; transform: translateY(-5px); }
                    100% { text-shadow: 0 0 5px blue, 0 0 10px blue, 0 0 15px blue; transform: translateY(0px); }
                }
                .glowing-text {
                    font-size: 40px;
                    font-weight: bold;
                    color: white;
                    text-align: left;  /* Align to the left */
                    animation: glow 1s infinite alternate;
                }
                </style>
                <h1 class="glowing-text">Most busy month</h1>
                """,
                unsafe_allow_html=True
            )

            # st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.markdown(
            """
            <style>
            @keyframes glow {
                0% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
                50% { text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red; transform: translateY(-5px); }
                100% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
            }
            .glowing-text {
                font-size: 40px;
                font-weight: bold;
                color: white;
                text-align: left;  /* Align to the left */
                animation: glow 1s infinite alternate;
            }
            </style>
            <h1 class="glowing-text">Weekly Activity Map</h1>
            """,
            unsafe_allow_html=True
        )
        # st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        # finding the busiest users in the group(Group level)
        if selected_user == 'Overall':
            st.markdown(
                """
                <style>
                @keyframes glow {
                    0% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
                    50% { text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red; transform: translateY(-5px); }
                    100% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
                }
                .glowing-text {
                    font-size: 40px;
                    font-weight: bold;
                    color: white;
                    text-align: left;  /* Align to the left */
                    animation: glow 1s infinite alternate;
                }
                </style>
                <h1 class="glowing-text">Most Busy Users</h1>
                """,
                unsafe_allow_html=True
            )
            # st.title('Most Busy Users')
            x,new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # WordCloud
        st.markdown(
            """
            <style>
            @keyframes glow {
                0% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
                50% { text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red; transform: translateY(-5px); }
                100% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
            }
            .glowing-text {
                font-size: 40px;
                font-weight: bold;
                color: white;
                text-align: left;  /* Align to the left */
                animation: glow 1s infinite alternate;
            }
            </style>
            <h1 class="glowing-text">Wordcloud</h1>
            """,
            unsafe_allow_html=True
        )
        # st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        most_common_df = helper.most_common_words(selected_user,df)

        fig,ax = plt.subplots()

        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')

        st.markdown(
            """
            <style>
            @keyframes glow {
                0% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
                50% { text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red; transform: translateY(-5px); }
                100% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
            }
            .glowing-text {
                font-size: 40px;
                font-weight: bold;
                color: white;
                text-align: left;  /* Align to the left */
                animation: glow 1s infinite alternate;
            }
            </style>
            <h1 class="glowing-text">Most commmon words</h1>
            """,
            unsafe_allow_html=True
        )
        # st.title('Most commmon words')
        st.pyplot(fig)

        # emoji analysis
        emoji_df = helper.emoji_helper(selected_user,df)
        st.markdown(
            """
            <style>
            @keyframes glow {
                0% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
                50% { text-shadow: 0 0 10px red, 0 0 20px red, 0 0 30px red; transform: translateY(-5px); }
                100% { text-shadow: 0 0 5px red, 0 0 10px red, 0 0 15px red; transform: translateY(0px); }
            }
            .glowing-text {
                font-size: 40px;
                font-weight: bold;
                color: white;
                text-align: left;  /* Align to the left */
                animation: glow 1s infinite alternate;
            }
            </style>
            <h1 class="glowing-text">Emoji Analysis</h1>
            """,
            unsafe_allow_html=True
        )
        # st.title("Emoji Analysis")

        col1,col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            # fig,ax = plt.subplots()
            # ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f")
            # st.pyplot(fig)
            emoji_df[0] = emoji_df[0].astype(str)

            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")

            # Set font to display emojis correctly
            plt.rcParams['font.family'] = 'Segoe UI Emoji'  # For Windows
            st.pyplot(fig)










