#!/usr/bin/env python
# coding: utf-8

# **GUID**: 2507608

# # Exploring the world in the 19th Century
# 
# ## Enhancing human creativity using AI to expand on the travel journals of a 19th Century Scottish gentleman
# 
# ![AI-generated cover art for 19th Century Travel Journal written by a Scottish gentleman](resources/generated_images/dall_e_sophisticated_cover.png)
# 
# _To generate this image, I used the journal transcript data to generate an image in DALL-E, included with ChatGPT Plus. The prompts I used were "Draw a cover for the travel journal" and "Draw another cover for the travel journal"._

# ## Introduction
# 
# What does a 19th century anonymous travel journal spanning less than five months tell us about travel in an era with no aeroplanes, high-speed trains and mobile internet? More importantly, what was left behind in the author's imagination, and how can we read between the lines and let our own imagination – and, crucially, the imaginations of a wide and varied audience – run wild?
# 
# Generative AI may have the answer to these questions.
# 
# This project seeks to leverage generative artificial intelligence (AI) to reimagine and expand upon the travels of an anonymous 19th-century Scottish gentleman that recorded his journey, along his family, to the South of France and Rome between March 1867 and 1868. The project seeks to combine travel journalling and the creativity of an author with generative technology, aiming to uncover, expand and reimagine the narratives hidden in a relatively obscure historical document.
# 
# Through providing audiences with an interactive application, using existing AI models, and training it with the journal data and metadata, we aim to provide with a tool to engage, not only with the entries, drawings and photos that the author left in the journal, but also tap into the latent creative visions and cultural insights that the author may have hinted at or entirely omitted. We propose a tool that, fine-tuned with 19th-century creativity, builds a bridge with modern audiences and allows them to expand that creativity through the use of technology.
# 
# This project seeks to demonstrate how human-AI collaboration can enhance human creativity and bring past experiences and modern perspectives closer.

# ## 1. Context
# ### 1.1. Historical and cultural background

# Travelling in the 19th century was neither accessible nor within the reach of all social classes. Leisure travel would often require substantial amounts of money and free time, resources available only to the upper classes in Britain and beyond.
# 
# Spare time was essential for travel, as it often involved spending several days in a diligence, public stagecoach, or a privately hired carriage and courier (Buzard 1993, 40). Travellers would make frequent stops, spending time  sightseeing, shopping, and attending cultural events in various places en route to their final destination.
# 
# While this remained true until the twentieth century, the nineteenth century witnessed an explosion in British tourism in Continental Europe facilitated by the end of the Napoleonic Wars (1803–1815) and the emergence of new steam-powered forms of transport, such as the steamboat and the railroad. 
# 
# The expansion and consolidation of these new means of transport between 1820 and 1850 facilitated the emergence of an industry centred around tourism and organised travel (Buzard 1993, 47). For example, Thomas Cook & Son became one of the pioneering firms to offer packages of transport, accommodation, and food tickets—what we know today as package holidays (Périz Rodríguez 2020). Cook aimed to simplify every aspect of travelling between Britain and continental Europe, as demonstrated by his agreement with French railway authorities in 1875. This agreement meant passengers no longer had to stop and reclaim their luggage at every transfer point (Buzard 1993, 41).
# 
# The development of coordinated steam-powered routes between Britain and continental Europe was uneven. Until at least the late 1840s, travellers from London to Paris had to use a combination of train, steamboat, and horse-powered diligence inside French territory. The last leg of the trip disproportionately increased the total travel time (Buzard 1993, 42). 
# 
# Nevertheless, by 1840, around 100,000 Britons crossed the English Channel annually (Buzard 1993, 41). Most began their journey on a cross-Channel vessel to Calais or Boulogne before proceeding to Paris (Heafford 2021, 380). Those embarking on a ['Grand Tour'](https://www.britannica.com/topic/grand-tour) would then continue to other major French and Italian cities (Zelazko 2024).
# 
# Proponents of the democratisation of travel and tourism, such as Thomas Cook, argued that it would bring economic benefits to regions visited by tourists (Buzard 1993, 45) and would help narrow the existing gap between social classes, ultimately fostering a national and even universal cultural brotherhood. Cook believed that travelling allowed ordinary people to grow and enrich themselves morally and culturally (Buzard 1993, 49).
# 
# The expansion of travel led to increased textuality among the growing travelling population; letters, telegrams, travel journals, war journalism, and booster literature soared in popularity, partly aided by the emergence of photography and stereographic images (Thompson 2019, 109). Many of these travel literary works were published, including ['A Trip to Paris and Belgium [Travel Sonnets]'](http://www.rossettiarchive.org/docs/54-1849.dukems.radheader.html) by Dante Gabriel Rossetti (1849), ['A Flight'](https://americanliterature.com/author/charles-dickens/short-story/a-flight), an account of one of Charles Dickens' trips between London and Paris published in the journal _Household Words_ (1851), and ['Pictures From Italy'](https://www.gutenberg.org/files/650/650-h/650-h.htm), a travelogue by Dickens (1846) that captures his reflections and impressions during a trip to France and Italy.
# 
# However, countless travel journals and memoirs remained unpublished. Many tourists, like the anonymous Scottish gentleman whose travel journals we will analyse, kept records (with varying rigour) of the rural and urban landscapes they visited, the people they met, and the activities they engaged in (Buzard 1993, 21). These literary works offer unique perspectives that help us understand how people experienced travel in the 19th century, how class divisions influenced travel, and how 19th-century tourism compares to today's.

# ### 1.2. Object chosen, cultural and historical significance

# #### 1.2.1. Chosen object: _Journal of a continental tour_ (Anonymous 1867-1868)
# 
# For this project, I have chosen a 19th-century manuscript travel journal with pen-and-ink drawings and photographs. It is stored in the Archives and Special Collections at the University of Glasgow with the reference code [GB 247 MS Gen 13](https://www.gla.ac.uk/collections/#/details?irn=250262&catType=C&referrer=/results&q=ms+gen+13). The journal is titled _Journal of a continental tour_ and was written between October 1867 and March 1868.
# 
# The object is a handwritten travel diary authored by an unidentified wealthy Scottish man. In the diary, the author narrates his travels to the South of France and Rome alongside his daughter and, presumably, his wife between October 1867 and March 1868.
# 
# In the journal, the author wrote nearly 20,000 words, created 11 pen-and-ink sketches depicting situations and people he encountered during his travels, and attached six early photographs. These photographs illustrate some of the places and individuals he described in the journal.
# 
# The journal is in an early 20th-century binding and was acquired by the University of Glasgow Library from John Smith on 18 November 1953. The general public can access it, but they must make an appointment with [Archives and Special Collections](mailto:library-asc@glasgow.ac.uk).

# #### 1.2.2. Historical and cultural significance of the object
# 
# First-hand testimonies of travels recorded in travel journals, correspondence and memoirs make up the gross of the sources used to interpret the experience of travellers and understand the practicalities involved (Heafford 2021, 374), particularly during times when travelling was the province of the wealthy and privileged.
# 
# While this object contains only the journals written by one specific (unnamed) author during his travels, the detailed records of the places he visited, the people he met, and the activities he engaged in provide an excellent starting point for understanding how travel has evolved since the 19th century.
# 
# This journal was written by a wealthy Scottish gentleman. It captures his personal experiences, thoughts, and opinions. While this document can be very useful in understanding how he and his family experienced travel, we must be cautious not to generalise these subjective experiences to all contemporary travellers. Although many experiences may have been similar, this dataset is too limited and subjective to conclusively represent travel in the 19th century.

# ## 2. Design Approach
# 
# ### 2.1. Project objectives
# 
# 1. This project aims to introduce a selected object—an obscure 19th-century manuscript travel journal stored in the University of Glasgow Library's Archives and Special Collections—to a wider audience.
# 2. The project seeks to leverage generative AI's storytelling capabilities to engage with the object in novel ways, offering new perspectives and interpretations of the textual and graphic data it contains.
# 3. Through innovative and interactive methods of engagement facilitated by AI, the project encourages audiences to critically reflect on the experience and accessibility of travel across the ages, as well as the similarities and differences between how travel was conducted in the 19th century and how it is conducted today.

# ### 2.2. Project approach – how we will meet the objectives
# 
# 1. **Research:**
# I have conducted research on 19th-century travel and travel journaling. I have also read the [transcript of the journal](dataset/transcript_robert_mclean.docx) that Robert McLean produced.
# 
# 
# 2. **Identify the optimal AI application(s) for this project:**
# Initially, I wanted to create my own AI application using the [Transformers](https://huggingface.co/docs/transformers/en/index) neural network architecture. I explored creating my own text generation model and [fine-tuning](https://huggingface.co/docs/transformers/en/training) a pre-trained model with the object data and metadata. However, my limited knowledge of Python and the overly specific documentation hindered my progress. The documentation available did not teach general principles but instead led me through predetermined tasks, which restricted my ability to utilise the object data. Subsequently, I decided to [create a GPT](https://help.openai.com/en/articles/8554397-creating-a-gpt) application using the object data and metadata.
# 
# 
# 3. **Data preparation:**
# Initially, I edited Robert McLean's transcription to remove any subjective decisions made during transcription (for example, comments regarding legibility of the manuscript or additional context) and uploaded it as a [CSV file](https://www.kaggle.com/datasets/emiliomoralesparedes/gb-247-ms-gen-131) to Kaggle, as I expected to train my text generation model with that data. I also added authorship, provenance, and license metadata to the dataset to make it freely available.
# When I decided to create a custom GPT, I uploaded the Robert McLean's transcription file to the custom GPT. I chose this file because it included placeholders for the images and photographs attached to the original object. Since the custom GPT would have access to DALL-E 3, I cropped and edited the photographs I had taken of the object's images and illustrations, and then uploaded them to the custom GPT.
# 
# 
# 4. **Text generation:** Using ChatGPT's GPT-4 model, fine-tuned with the object data and metadata, we aim to broaden the journal's scope. I have provided "conversation starters"—prompts that I pre-wrote to show users various ways they can engage with the transcript. These prompts are designed to leverage the text style transfer capabilities of the GPT-4 model to extend human creativity beyond what was recorded in the journal. Utilising ChatGPT for this application offers additional benefits: many users are familiar with the tool and are likely to engage with the application in creative ways not anticipated during the project design stage, thus enabling new perspectives and interpretations of the object data and metadata, and enhancing the storytelling capabilities of the journal.
# 
# 
# 5. **Image generation:** ChatGPT Plus includes access to DALL-E 3, a text-to-image model that is fully integrated with GPT-4. We will use DALL-E 3 to generate new photorealistic images and sketches based on the data included in the journal, as well as new images in the styles of the drawings and photographs already present in the journal, depicting places and situations not covered in the original entries. The aim is to offer new ways of engaging with the object data and to encourage reflection on the experience and accessibility of travel across different eras. I have provided prompts that users can use to generate images. However, DALL-E 3 offers countless possibilities, and users will be able to enter their own inputs, thus extending the creative applications of the journal data.
# 
# 
# 6. **Further AI applications:** There are further applications of generative AI models that can provide novel ways and creative ways of engaging with the object data and introduce it to a wider audience, such as text-to-speech generation and text-to-video generation. However, we will only explore these briefly.
# 
# ![Custom GPT application settings](resources/images/application_settings.png)
# _Custom GPT application settings._
# 

# ### 2.3. Human component
# 
# This is a human-AI collaboration project designed to provide easy-to-use interfaces for generative AI models. Its purpose is to extend the creativity captured in the journal of a 19th-century author beyond his original recordings, enabling audiences to engage critically with the object data and generate new content using creative prompts.
# 
# The key components of this project are human-made, including the object data, created by an unidentified wealthy Scottish man in the 19th century and manually transcribed for the University of Glasgow Library by  [Robert McLean](https://www.gla.ac.uk/stafflist/search/person/48dce7e28494/). Another critical element is the creativity of users who interact with the object through the custom GPT application I have developed.
# 
# While the technology underlying this project facilitates text and image generation, the applications require human-made text prompts to produce novel outputs.

# ### 2.4. Technologies used
# 
# #### 2.4.1. ChatGPT Plus
# [ChatGPT](https://openai.com/chatgpt) (Generative Pre-Trained Transformer) is a conversation-based AI text generation application that uses the GPT 3.5 and GPT 4 models, developed by [OpenAI](https://openai.com/).
# 
# The GPT-3.5 and GPT-4 models are large language models (LLMs) based on the Transformer architecture designed by engineers at Google in 2017 (Vaswani et al 2017). LLMs are the foundation of text generation–they are pre-trained Transformer models that have been trained to predict the next token when provided an input. 
# 
# In the Transformers architecture, each Transformer model typically consists of an encoder and a decoder. Each Transformer layer within the encoder and decoder consists of two key components: a self-attention mechanism and a feedforward neural network. The self-attention mechanism assigns weights to each input word, effectively capturing the relationships between all words in the sequence. This mechanism allows the model to focus on different parts of the sequence for different tasks. The feedforward neural network processes the inputs independently and in parallel, using the outputs from the self-attention mechanism, which integrates information about the relationships and relevance of different parts of the input sequence. This processed output is then transformed into a new representation that feeds into the next layer of the network.
# 
# ![Transformers Architecture](resources/images/transformers_architecture.png)
# _**Source:** ['Attention Is All You Need'](http://arxiv.org/abs/1706.03762)_
# 
# Both GPT-3.5 and GPT-4 have been designed and trained to engage in natural language conversations. Users can interact with the models through the ChatGPT interface by entering prompts and asking questions in natural language. ChatGPT is used by over 100 million people weekly (Heath 2023), making it a familiar interface for many potential users of the application I have designed.
# 
# OpenAI offers GPT-3.5 for free, but using GPT-4 requires a subscription to [ChatGPT Plus](https://openai.com/blog/chatgpt-plus) at $20 per month. ChatGPT Plus also enables the creation of custom GPT applications based on GPT-4, incorporating custom 'knowledge' such as text, images, files, and datasets.
# 
# In order to create a custom GPT using the object data and metadata, I have subscribed to ChatGPT Plus.

# #### 2.4.2. DALL-E 3
# 
# [DALL-E 3](https://openai.com/dall-e-3) is a text-based image generation AI model developed by OpenAI that uses a diffusion model architecture. This model starts with a noise pattern and progressively refines it into a coherent image that corresponds to the input text description. The process does not directly involve an encoder-decoder architecture of traditional autoencoders but rather transforms noise into detailed images through a series of learned steps, capturing the key features described in the text.
# 
# DALL-E 3 is built natively on ChatGPT and it is available to ChatGPT Plus subscribers as part of the monthly subscription.
# 
# Users can use natural language prompts to generate novel images using the object data and metadata I have used to fine-tune the model.

# #### 2.4.3. Narakeet
# 
# [Narakeet](https://www.narakeet.com/) is a text-to-speech commercial application, formerly known as Video Puppet. Although Narakeet does not publicly disclose the architecture on which its service is based, it provides a user-friendly interface that allows users to input text scripts and generate voiceovers.
# 
# Using Narakeet for text-to-speech in this application is interesting, as Narakeet is one of the few commercially available services that offer Scottish accents for voice generation. Specifically, it provides two adult male voices, two adult female voices, one child male voice, and one child female voice.

# #### 2.4.4. VEED.io and Invideo AI
# 
# Both [VEED.io](https://www.veed.io/) and [invideo AI]() are AI-powered text-to-video applications that streamline video production using text inputs. VEED.io specialises in creating realistic video voiceovers from text. On the other hand, Invideo AI generates scripts from textual inputs and sources relevant stock images and videos, combining these elements into complete videos with voiceovers.
# 
# Neither VEED.io nor Invideo AI publicly discloses the architectures on which their services are based, yet both platforms facilitate the creation of video content derived from simple text descriptions.

# ## 3. Application
# 
# ### 3.1. Accessing the application
# The application is available to ChatGPT Plus subscribers through [this link](https://chat.openai.com/g/g-BtyUH4oNv-19th-century-travel-journal-gpt). ChatGPT Plus subscribers can also access it from the 'Research & Analysis' category in the ChatGPT GPT Store.

# ### 3.1.2. Application interface
# As this is a custom GPT application created within the ChatGPT interface, the application interface is almost identical to the default ChatGPT Plus interface. The only discernible differences are:
# 
# - The title of the application is displayed instead of the name of the model (GPT-3.5/GPT-4).
# - The name of the author of the application is displayed.
# - The application presents four 'conversation starters'—preset prompts to show users what they can do with the application.
# 
# ![Custom GPT application interface](resources/images/application_interface.png)
# _Custom GPT application interface._

# ### 3.1.3. Application metadata
# 
# As explained in section 2.2, I fed the custom GPT application the object's metadata I had access to. I was worried that the underlying GPT-4 model would try to use the metadata, so I saved the metadata on a txt file, providing context and explicit instructions at the beginning of the file:
# 
# >METADATA – THIS FILE IS TO BE INDEXED ONLY, NOT TO BE USED TO GENERATE JOURNAL RESPONSES
# >
# >The file 'transcript_robert_mclean.docx' contains the transcript of 'Journal of a continental tour', a 19th-century manuscript travel journal with pen-and-ink drawings and photographs.
# >
# >'Journal of a continental tour' is stored in the Archives and Special Collections at the University of Glasgow with the reference code GB 247 MS Gen 13. 
# >
# >'Journal of a continental tour' was written between 1867 and 1868. It is a handwritten travel diary authored by an unidentified wealthy Scottish man. In the diary, the author narrates his travels to the South of France and Rome alongside his daughter and, presumably, his wife between October 1867 and March 1868.
# >
# >In 'Journal of a continental tour', the author drew 11 sketches using pen and ink depicting situations and people he encountered during his travels. He also attached six early photographs to the diary, illustrating some of the places he described in the journal and the people he met in his travels.
# >
# >The files containing pen and ink sketches are:
# >- 'coming_ashore.jpeg'
# >- 'couple_packing.jpeg'
# >- 'heavily_loaded_coach.jpeg'
# >- 'mosquito_hunting,jpeg'
# >- 'moustached_man.jpeg'
# >- 'mr_gilchrist_and_wife'.jpeg
# >- 'mrs_keiths_daughter.jpeg'
# >- 'nice_woman.jpeg'
# >- 'seasick_passengers.jpeg'
# >- 'seasick_passengers_2.jpeg'
# >- 'seasick_passengers_3.jpeg'
# >
# >The files containing photos are:
# >- 'admiral_farragut_photo.jpeg'
# >- 'beach_and_small_town_photo.jpeg'
# >- 'eza_small_photo.jpeg'
# >- 'mentone_photo.jpeg'
# >- 'sir_george_bell_photo.jpeg'
# >- 'turbia_photo.jpeg'
# >
# >'transcript_robert_mclean.docx' includes contextual placeholders for all pen and ink sketches and photo files.
# >
# >'Journal of a continental tour' is in an early 20th-century binding and was acquired by the University of Glasgow Library from John Smith on 18 November 1953.
# 
# I understand that this is not a standard way of feeding metadata to a generative AI model, but I could not find documentation that explained the best way of doing so.
# 
# However, my approached may have worked. When giving the prompt "What is the metadata of the journal?", the mapplication gave me the following response:
# 
# >The journal titled "Journal of a continental tour" is a 19th-century manuscript that records a travel diary authored by an unidentified wealthy Scottish man. It covers his travels with his daughter and presumably his wife to the South of France and Rome from October 1867 to March 1868. The journal is stored in the Archives and Special Collections at the University of Glasgow under the reference code GB 247 MS Gen 13. It includes 11 sketches made with pen and ink and six early photographs that depict scenes and people the author encountered during his travels. The journal itself is in an early 20th-century binding and was acquired by the University of Glasgow Library from John Smith on November 18, 1953.
# 
# ![Custom GPT application interface](resources/images/metadata.png)
# _Application answering a metadata-related prompt._

# ### 3.1.4. Generating novel journal entries
# 
# One of the most interesting applications of generative AI in text is its ability to generate outputs that mimic the style described in the prompts or in the data used to fine-tune the model. This capability allows for creative applications such as writing in the tone or manner of a particular genre or author.
# 
# Given that the journal ended abruptly in March 1868, it would be interesting to use our custom GPT application to imagine what an entry for a different city would look like.
# 
# With that in mind, I have used one of the 'conversation starters' to prompt the application to generate a novel journal entry for a European city not mentioned in the original journal:
# 
# > Write a new journal entry for a different European city in the style of the author
# 
# The resulting output is as follows:
# 
# >Prague, 18th April 1869
# >
# >This morning, after an early repast at our modest yet curiously comfortable quarters at the "Golden Stag," we set out to explore the splendors of Prague, a city of such historic weight that every cobblestone seems to bear a tale. The air was crisp, and the streets began to swell with the bustle of the Bohemian populace, their dialects as varied as the architecture that framed our meandering path.
# >
# >Our first endeavor was to ascend the heights of Hradčany, to behold the grandeur of Prague Castle. The ascent was steep and my spirits soared with every step, as the city’s panorama unfurled beneath us like a living tapestry. Upon reaching the castle, the vastness of its courtyards and the stern beauty of its stonework were a formidable sight. We lingered in the shadows of St. Vitus Cathedral, where the light danced through stained glass, casting kaleidoscopic patterns that seemed almost divine.
# >
# >Wandering further, we descended into the Lesser Town, crossing the famed Charles Bridge, a marvel of medieval engineering now lined with the stoic statues of saints who gaze eternally upon the flowing Vltava. Vendors and artists claimed every nook, their wares as colorful as the tales they spun to passersby.
# >
# >Lunch was had at a quaint eatery by the riverside, where we indulged in the local fare of roasted duck and dumplings, a hearty meal that promised enough sustenance for our afternoon's exertions. Refreshed, we ventured into the Old Town, its square dominated by the Astronomical Clock. As the hour struck, a crowd gathered to watch the mechanical performance of figures that marked the passage of time—a spectacle that brought both locals and travelers together in shared wonder.
# >
# >The day waned as we meandered through narrow lanes, each turn revealing scenes worthy of a painter's canvas. We stumbled upon a small shop filled with Bohemian glass, the pieces glinting like jewels under the shop’s dim lights. I could not resist procuring a small, intricately etched vase as a tangible memory of this city’s artisanal spirit.
# >
# >As twilight embraced the city, we retired to a local tavern for supper. Over mugs of dark, frothy beer, we recounted the day's adventures, the laughter and camaraderie an echo of the vibrant life that pulses through Prague's historic heart.
# >
# >Thus we ended our day, under the watchful gaze of a crescent moon, Prague’s rooftops a jagged silhouette against the starlit sky. Tomorrow promises further explorations, but for tonight, we rest, hearts and minds full of the day’s enchantments.
# 
# With 416 words, this journal entry is longer than most entries found in the original journal. Upon reading the entry, we can ascertain that it is not written in a modern style. If we look closely and compare some of the word choices, such as verbs and adjectives (for example, 'set out', 'crisp', 'meandering', 'ascend', 'unfurled', 'famed', 'quaint', 'indulge', among others), we can see that only a few of these words are used in the original journal: 'set out', 'ascend', 'indulge', 'hearty', and 'promised'. Crucially, the original author used 'dinner' to refer to the last meal of the day, while the GPT model used the term 'supper'.
# 
# This quick analysis reveals that, although the application succeeds in creating a new, plausible journal entry for a 19th-century travel journal, it does not completely capture the style of the author of the source material.
# 
# ![Generating new journal entries](resources/images/text_generation_1.png)
# _Generating new journal entries using a 'conversation starter'._
# 
# I have also tested the preset prompt I added to the application to generate more details about any specific event described in the journal:
# 
# > Expand on any particular event described in the journal in the style of the author
# 
# The output generated by the GPT application is the following:
# 
# >Expanding on an event from the journal, we delve deeper into the journey's challenges and the rich sensory experiences encountered by our Scottish traveler and his family as they ventured from the familiar comforts of their Glasgow home to the sunny climes of the Mediterranean. Here's an expanded narrative based on the author's style:
# >
# >---
# >October 29, 1867, marked the beginning of an odyssey laced with both anticipation and apprehension. The day dawned dreary and wet, a somber Scottish farewell as we embarked from Glasgow. The hours preceding our departure were fraught with the chaos typical of Victorian travel; the house was awash with the clutter of packing trunks, the perpetual rustling of garments, and the clinking of glass as bottles of port were carefully stowed away, each item meticulously considered for its necessity and then packed away with a mixture of dread and necessity.
# >
# >Our journey to the Charing Cross Hotel in London was accompanied by the relentless pounding of rain against the windows of our carriage, an unyielding reminder of the comforts we had forsaken. Miss Wingate, a young relative of Sir George, shared our compartment. Her quiet presence, a stark contrast to the storm outside, provided a silent solace amid the turbulence.
# >
# >Upon reaching London, the true test of our resolve began. The cacophony of the bustling city, the sodden streets, and the dreary skies above did little to lift our spirits. The next leg of our journey to Nice via Paris was marked by a rough crossing to Boulogne. The steamer, though superior to others, swayed and creaked under the force of the previous night's storm. The swell was considerable, bringing about the usual unpleasantness among passengers. My wife and daughter, along with others, suffered the effects of the sea, though Margaret bore the ordeal with commendable stoicism, staying by my side on deck.
# >
# >The human drama unfolding around us was a spectacle of its own. Newlywed couples, their joy quickly turning to seasick misery, and families clutching to each other, all painted a vivid picture of Victorian travel's trials. One particular gentleman, wrapped in a Turkish blanket, his dignity assaulted by the waves, caught my attention. His expression, a blend of anger and resignation, was a poignant symbol of our collective plight.
# >
# >Arriving in Boulogne brought no respite, as the struggle with luggage and customs awaited. Our grand bags, though registered to Paris, were but a fraction of our encumbrance. The numerous smaller packages, each a testament to the Victorian penchant for over-preparation, were a burden I bore through the crowded docks, my mind filled with second thoughts about the wisdom of our journey.
# >
# >As we finally made our way to the train bound for Paris, a weary sense of accomplishment settled over us. The ordeal of departure was behind us, and ahead lay the promise of the Riviera's warmth. Yet, as the French countryside sped by, I could not shake the lingering doubts. Was the sacrifice of home comforts justified by the pursuit of health and adventure? Only time would tell if the sunnier climes would prove a sufficient balm for the sacrifices made.
# >
# >Our stay in Paris was brief but recuperative, a necessary pause in the relentless pace of travel. The city, with its vibrant streets and elegant cafés, offered a stark contrast to the dreary days spent in transit. Yet, the shadow of home lingered, the memory of our quiet life in Glasgow a stark backdrop to the bustle of Parisian life.
# >
# >As we continued our journey south, each mile traversed was a step further from the familiar and a step deeper into the unknown. The Mediterranean awaited, its famed beauty a balm to our weary spirits. Yet, as the train carried us further from home, the question remained—would the beauty of the South prove equal to the trials of the journey?
# >
# >---
# >This expanded entry strives to maintain the authenticity and introspective nature of the original journal, while offering a richer narrative of the emotions and experiences faced by our travelers.
# 
# 
# While the application generated a coherent and detailed response, it did not follow the instructions I provided, since it described events from different days. However, when clarifying what I expect to see, it generates a more appropriate response.
# 
# I provided this prompt as follow-up:
# 
# >Now, expand one single event described in the journal, providing richness of detail.
# 
# To which the application replied:
# 
# >Let's expand on a specific event: the dramatic and often humorous scene during the crossing from London to Boulogne, focusing on the memorable interaction and observations concerning the newlywed couple on the steamer. Here is a deeper narrative exploration of that event:
# >
# >---
# >On the chilly morning of October 30, 1867, as we boarded the steamer Albert Edwards, bound for Boulogne, the remnants of the night's storm yet whispered threats in the gusts and choppy waters of the Channel. The vessel, though robust and reputedly superior, was rocked by swells that churned the stomachs of many a seasoned traveler and novice alike.
# >
# >Among the passengers, a couple, notably fresh in their matrimonial bonds, caught my observant eye. The young bridegroom, a figure of respectable appearance with a demeanor that bespoke both nervousness and pride, supported his bride with a tenderness that the rough seas seemed determined to test. His bride, a young lady of no extraordinary beauty, possessed a complexion which, under the strain of the voyage, transitioned from a maidenly pallor to a most unfortunate shade of green.
# >
# >As the vessel heaved, so too did the spirits of the passengers wane. The bride, initially seated upright beside her attentive husband, soon succumbed to the relentless rocking of the ship. Her condition deteriorated until she lay listlessly in her husband's arms, her face a canvas of seasick misery. The husband's expression, one of rueful compassion, did little to mask his own discomfort at the situation, which the sea's rough embrace only intensified.
# >
# >From our vantage near the funnel—where the air was mercifully clear and the heat offered some respite from the chill—I sketched the scene. The juxtaposition of youthful optimism against the grim reality of seasickness provided a rich tableau of human experience. Nearby, other characters added to the drama: a nurse, her fashionable bonnet askew as she tended to a distressed child; a stern-looking gentleman, perhaps Dutch, who maintained a stoic silence despite his evident suffering; and a distinguished foreigner, swathed in a Turkish blanket, who regarded the tumultuous scene with a fierce, if seasick, dignity.
# >
# >The crossing, while brief in the span of our journey, was an ordeal that etched itself deeply into my memory. The steamer's deck became a stage upon which the varied responses to discomfort and distress played out, each passenger contributing to a broader portrait of human resilience and vulnerability.
# >
# >As Boulogne finally came into view, the relief was palpable. The ordeal of the crossing had tested the mettle of all on board, and while the physical discomforts might soon fade, the memories of that challenging passage would linger, a vivid chapter in the narrative of our travels.
# >
# >---
# >This entry provides a deeper glimpse into the humor and pathos of travel in the 19th century, capturing the character and atmosphere of a particular moment that reflects broader themes of the travel experience.
# 
# Using the accounts written by the journal's author as a starting point, the custom GPT application vividly tells a story that fills in the blanks left by the author. Audiences are able to see the author's experiences brought to life – or even generate descriptions of places the author did not dream visiting – through the storytelling capabilities of GPT-4.
# 
# If what we want to do is to compare how people experienced travel in the 19th century and how people experience it now, based on the journal entries, we can ask the following prompt:
# 
# >How would a 21st century traveller experience the travels described in the journal?
# 
# To which the application responded:
# 
# >A 21st-century traveller retracing the journey described in the 19th-century travel journal would experience a significantly different adventure, shaped by modern conveniences and cultural shifts. Here's how their experience might differ:
# >
# >**Transportation Advances**: The original journey, characterized by long and arduous train rides, steamships, and horse-drawn carriages, would today be replaced by faster and more comfortable trains, flights, and car rentals. Modern infrastructure would make travel between cities quicker and less physically taxing.
# >
# >**Accommodations**: While the journal describes stays in various hotels and pensions, often with issues of comfort or service, today’s traveller would have a wide range of options from luxury hotels to budget-friendly Airbnbs. Modern amenities such as WiFi, air conditioning, and online booking would streamline the travel experience.
# >
# >**Cultural and Social Changes**: The social and cultural landscape that forms the backdrop of the journal has transformed considerably. Cities that were once small or modest in size may now be bustling metropolises, and many historical sites might now be preserved as tourist attractions. The traveler of today would also encounter a more diverse array of cuisines and languages than a 19th-century traveller would.
# >
# >**Technological Enhancements**: Today's traveller would likely document their journey digitally, using smartphones, digital cameras, and social media, unlike the journal’s author who used pen-and-ink sketches and early photographs. Navigation would be aided by GPS rather than relying on local guides or paper maps.
# >
# >**Health and Safety**: The concerns of travel health that the journal mentions, like the need to carry port wine or the risks of sea travel, are mitigated today by advanced healthcare services available to travellers and improved safety standards in travel.
# >
# >**Tourism Development**: Many of the locations described as remote or exotic in the journal are now well-established tourist destinations. This means more crowds and commercialization but also better preservation of historical sites.
# >
# >**Environmental Awareness**: Modern travellers are more aware of their environmental impact. The journal's narrative of exploration and adventure would today be tempered by considerations of sustainable travel practices.
# >
# >Overall, while the essence of discovery might remain the same, a contemporary journey along the path of the 19th-century journal would be marked by ease, speed, comfort, and a different set of cultural insights, reflecting the profound changes over the last century and a half.
# 
# Granted, this may not be the most creative use of generative AI, but it certainly invites reflexion, and helps us engage with the content of the journal from a different perspective.
# 
# We can get more creative, and ask the application to "write a haiku based on the journal". To which it responds:
# 
# >In a journal quaint,
# >Misty seas and landscapes faint,
# >Old tales, ink sates heart.
# 
# This is only a taste of the storytelling capabilities of this custom GPT application. There is so much more that this application can do, such as writing poems or film scripts based on travel journals and sci-fi stories that bridge the 19th century with the present time, to name just a few of the possibilities with generative AI. These are also engaging and creative ways of interpreting the travel journal, which could help bring it closer to a new audience.

# ### 3.1.5. Generating novel drawings and photographs
# 
# The journal contains 11 pen-and-ink sketches and six photographs, all depicting scenes, people, and experiences the author and his family encountered during their travels. These visual elements enhance the journal's appeal by offering a window into life 150 years ago.
# 
# Images often speak louder than words. However, despite the author's eventful journeys, he gradually reduced his sketching over time. The journal includes only a few photographs, most of which capture distant landscapes.
# 
# We can employ, thus, our custom GPT application to generate new sketches and photographs, depicting scenarios, people, and locations that the author did not originally sketch or photograph.
# 
# When using the preset prompt "Draw a sketch of an action described in the journal in the style of the author's sketches included in the journal", we got the following output:
# 
# >Based on the descriptions in the "Journal of a continental tour," a suitable scene to sketch in the style of the author's pen and ink drawings might be the couple enduring the unpleasant sea voyage described in the text. The sketch could show the woman, who initially appears "all smiles and roses" at her wedding, now struggling with seasickness and appearing "green" in complexion, lying back in the arms of her husband during the remainder of the passage. The husband gazes at her with a rueful expression, capturing the contrast between their initial joy and current discomfort.
# >
# >Let me create the drawing for you.
# >
# >![Generated image 1](resources/generated_images/generated_image_1.png)
# >Here's the pen and ink sketch depicting a scene from the sea voyage described in the journal. The drawing captures the woman appearing seasick in the arms of her husband, who looks on with concern.
# 
# My first impression is that the image, while a sketch, has not been drawn using simple strokes, as the sketches drawn by the journal's author. However, we've not specified that we want simple strokes, either.
# 
# Let's take a look at the text prompt that the application has generated in the backend in order to generate the image using the DALL-E 3 model:
# 
# >A 19th-century pen and ink sketch depicting a scene on a steamship during a sea voyage. A young woman, dressed in period attire, appears seasick and green in complexion, lying back in the arms of her concerned-looking husband. The husband, also in period attire, gazes down at her with a rueful expression. The setting is the deck of the steamship with other passengers visible in the background, some also appearing seasick. The style is simple with fine lines and minimal shading, typical of personal travel journals from the 19th century.
# 
# We can see that the application has specified "the style is simple with fine lines and minimal shading", but the style is much more elaborated than the sketches we can find in the journal.
# 
# Fortunately, the author sketched the same scene, so, in this case, we have something to compare the generated images like for like:
# 
# >![Seasick passengers](dataset/images/seasick_passengers.jpeg)
# 
# 
# 
# When we specified in our prompt that we wanted simple strokes and a 'travel sketching' style, we got the following output:
# 
# >![Generated Image 2](resources/generated_images/generated_image_2.png)
# 
# While the generated image is much less detailed than the first image the application generated, it is still much more detailed than what the author drew.
# 
# Let's take a look at the prompt generated by the application:
# 
# >A travel sketch in a simple, expressive style, depicting a seasick woman in 19th-century attire, reclining in the arms of her concerned husband on the deck of a steamship. The couple are surrounded by a few other seasick passengers, creating a dynamic and slightly chaotic scene typical of a sea voyage. The drawing should use simple strokes and minimal detail to convey the discomfort and environment effectively, reflecting a personal and immediate impression captured by a traveler.
# 
# We can see that, this time, the application has followed our instructions and specified that the output should "use simple strokes and minimal detail". However, these prompts may not be detailed enough for DALL-E 3 to generate a sketch in the style of the journal's author's drawings. Or perhaps we have not fed the model enough sketches to identify the particular style of this author. If that is the case, I'm afraid that there is no easy solution, as we have uploaded digitised versions of all the images present in the journal and we do not know the identity of the author.
# 
# One observation stands out across all images – the author's original drawing and the generated images: they all present a very similar composition of a seasick young bride being held in arms by her groom.
# 
# Could it be that DALLE-3 "understood" the composition of the digitised sketch (which was not tagged beyond being named similarly to the placeholder that Robert McLean included in his transcription) and tried to replicate it? Or did it follow the description that the author gave in the journal entry?
# 
# Let's do a quick experiment. On a new session of our custom GPT application, I will request that it generates a photorealistic image based on the description provided by the author. I will use the following prompt,providing the full description given by the journal's author:
# 
# >Create a photorealistic image based on this description: 
# >
# >"There was a couple opposite to use – evidently newly married – who attracted a large share of our attention. Milady at the best was not good looking (which the bridegroom was) and what was at first a great paleness settled into a thorough greenness of complexion which must have been deeply interesting to her amiable companion. She lay back at last in his arms during the remainder of the passage while he contemplated her with a very rueful expression[...]"
# 
# The resulting output is as follows:
# 
# >![Generated Image 3](resources/generated_images/generated_image_3.png)
# >Here is the photorealistic image depicting the scene of a seasick bride on a boat, reclining in the arms of her concerned groom, as described from the 19th-century journal entry. The setting shows a stormy day on the deck of a large steamer.
# 
# And the prompt generated by the application is:
# 
# >A photorealistic image depicting a seasick bride on a boat. She is pale with a complexion turning green, dressed in late 19th-century attire, reclining in the arms of her handsome, well-dressed groom. The groom, looking concerned, gazes at her with a rueful expression. The setting is the deck of a large 19th-century steamer, with ocean and grey skies in the background, suggesting a stormy day. The bride's hair and attire should be visibly affected by the wind.
# 
# And if I enter, on a new session of the application, the following prompt:
# 
# >Create a photorealistic image based on the description of the young married couple in the steamer that the author provides
# 
# We get the following output:
# >To create a photorealistic image of the young married couple from the steamer as described in the journal entry, let's consider the detailed description provided:
# >
# >The couple, notably new in their marriage, presents a contrast in their disposition during a somewhat rough sea journey. The wife, described as initially very pale, transitions into a distinctly green complexion due to seasickness, a detail that emphasizes her discomfort. She eventually rests, lying back into her husband's arms, who watches her with a rueful and concerned expression. The husband, notably better looking than his wife, displays a mix of affection and worry as he contemplates her state.
# >
# >Based on this description, the image would capture the wife in a reclined position in her husband's arms, her face showing signs of seasickness, while the husband looks on with a mixed expression of love and concern. The setting would be on a steamer's deck, adding elements like the sea or parts of the ship to contextualize the scene. Let's proceed to create this image.
# >![Generated Image 4](resources/generated_images/generated_image_4.png)
# 
# With the following prompt generated by the application:
# >A photorealistic image depicting a young married couple on a steamer deck during the 19th century. The wife, pale and showing signs of seasickness with a greenish complexion, is reclined in her husband's arms. The husband, a good-looking man, gazes at her with a rueful and concerned expression. They are dressed in 19th-century attire suitable for travel. The background shows elements of a ship's deck and the sea, capturing the mood of a rough sea journey.
# 
# While we cannot know for sure from this experiment if DALLE-3 has recognised the composition of the sketch drawn by the author, it does not seem like it has added other passengers to the composition based on the context of the journal entry.
# 
# What we do know is that this application allows us to cross the boundaries of the author's creativity and visualise scenes that he described with much more detail.
# 
# This is even more evident when we request the application to generate an image based on descriptions found in the journal but for which the author did not draw a sketch. For example, using the prompt:
# >Draw a sketch of a Monaco casino using simple strokes in the style of the author using the descriptions found in the journal.
# 
# We get the following output:
# >The Monaco Casino, as envisioned by our journal's author, can be depicted in a pen and ink drawing using simple strokes. Let's consider the scene: the grand facade of the casino emerges prominently, its architecture reflecting the opulence of late 19th-century European design. Imagine large arched windows and ornate detailing around them, perhaps some intricate stonework that captures the light. The entrance is bustling with well-dressed gentlemen and ladies of the period, giving a glimpse into the lively social scene typical of such an establishment.
# >
# >A few ornamental trees might line the approach, adding a touch of elegance to the drawing. The overall atmosphere would be one of sophisticated charm, with a bustling yet refined crowd, all set against the dramatic architecture of the casino.
# >
# >Let's create this image.
# >![Generated Image 5](resources/generated_images/generated_image_5.png)
# >Here is the pen and ink sketch of the Monaco Casino, created in the style of a 19th-century travel journal. The drawing captures the grand architecture and the elegant atmosphere of the scene, with well-dressed gentlemen and ladies around the building.
# 
# While the sketch does not follow the style used by the journal's author, it brings to life a scene that the author did not draw, illustrating to new audiences what the author may have experienced during his travels, which he may not have described in detail.
# 
# The prompt generated by the application is:
# 
# >A pen and ink drawing of the Monaco Casino in the style of a 19th-century travel journal. The casino is depicted with grand architecture, featuring large arched windows and ornate stonework. Elegantly dressed gentlemen and ladies from the late 1800s are seen entering and exiting the building. Ornamental trees line the pathway, enhancing the opulent and lively atmosphere. The sketch uses simple strokes to capture the sophisticated charm of this historical setting.
# 
# We can now ask the application to "recreate one of the images of the diary but in modern times", it provides the following output:
# 
# >![Generated Image 6](resources/generated_images/generated_image_6.png)
# >
# >Here's a modern reinterpretation of a 19th-century travel journal image. This illustration features a group of tourists disembarking from a high-tech hovercraft onto a beach, surrounded by futuristic architecture, yet they're dressed in old-fashioned travel attire and using modern gadgets like holographic maps. The setting contrasts sharply with the historical clothing style, bringing a unique twist to the travel journal theme.
# 
# It's interesting to see what the application understands as modern – could it be what it believes was considered modern (and furutistic) in the 19th century?
# 
# The prompt that the application generated gives us some clues of its thought process:
# 
# >Modern version of a 19th century travel journal image, depicting a group of tourists embarking from a high-tech hovercraft onto a beach in a bustling seaside city with futuristic architecture. The scene captures the contrast between old-fashioned travel attire and the high-tech environment, showing tourists in 19th century style clothing with modern gadgets like holographic maps and digital cameras, against a backdrop of tall, sleek buildings and flying cars overhead, in a vibrant, detailed pen and ink style.
# 
# If we take a specific element of the journal entries, like the food the author and his family had during his travels – which he often describes in great detail, we can even try to bridge the 150-year gap with modern audiences, and show how that food may look like today.
# 
# When using the prompt:
# 
# >Choose one of the meals described in the journal (often described as "table d'hote") and draw an illustration showing how the entire meal would look like in a 21st century street food market
# 
# 
# The result is the following:
# 
# >In the journal, a meal described during a stay at a hotel includes a table d'hôte menu consisting of soup, stewed tongue, roast fowl, stewed celery, roast beef with salad, crème de vanille and sweet biscuits, and a dessert of grapes. Here's how I imagine this meal would look at a 21st century street food market:
# >
# >Prompt for image generation:
# >"Imagine a bustling 21st-century street food market with a modern twist on a 19th-century meal. In the foreground, a vibrant food stall displays an updated version of a traditional table d'hôte meal. The stall is adorned with chalkboard menus and rustic wooden decor, reflecting a hip, urban vibe. The meal includes a small bowl of artisanal soup, creatively presented stewed tongue tapas, gourmet mini roast fowl sliders, a side of sautéed celery, a stylish roast beef salad with fresh greens and vinaigrette, and mini jars of crème de vanille. The dessert section showcases a platter of grapes alongside freshly baked sweet biscuits, all served on eco-friendly, stylish dishware. The background buzzes with a diverse crowd of young urbanites enjoying their meals on communal tables, under string lights, with the city skyline faintly visible in the evening light."
# >
# >Let's create this image.
# >![Generated Image 7](resources/generated_images/generated_image_7.png)
# >
# >Here's the illustration of how a 19th-century table d'hôte meal would look in a 21st-century street food market setting. The image captures a modern and vibrant food stall presenting a creatively updated version of the historical meal.
# 
# This is a really impressive interpretation of one of the meals described by the author, and one that will surely resonate more with modern audiences than a traditional 'table d'hôte'.
# 
# Lastly, if we want to imagine how the author and his family would look if they were modern travellers, we can ask the application to "generate a photorealistic photo of the author and his family as 21st century tourists".
# 
# And we get the following result:
# >![Generated Image 8](resources/generated_images/generated_image_8.png)
# >Here is the photorealistic image of a Scottish family dressed as 21st-century tourists, visiting a modern European city. You can view the family in front of a contemporary landmark, enjoying their tour.
# 
# The prompt generated is the following:
# >A contemporary family photo of a Scottish family dressed as 21st-century tourists, visiting a modern European city. The family consists of a middle-aged man and woman, and a teenage girl. The man is wearing a casual polo shirt, jeans, and sunglasses, holding a digital camera. The woman is stylishly dressed in a summer dress and wide-brimmed hat, carrying a tote bag. The girl, in trendy attire, is using a smartphone. They are standing in front of a famous modern landmark, such as the Louvre Pyramid or a similar structure, suggesting they are tourists.
# 
# The modern representation of the author is carrying a camera – perhaps he does not need to draw sketches anymore.
# 
# These are just a few examples. The possibilities for generating creative images, however, are endless. Audiences can use their imagination, and craft and share a prompt with the application and observe how their creativity comes to life thanks to generative AI.

# ### 3.1.6. Letting imagination run wild with other AI applications
# 
# The storytelling capabilities of generative AI are endless. If generating new journal entries or new sketches to illustrate the author's travels was impressive, other generative AI applications can augment human creativity, resulting in deeply engaging applications that combine AI-generated images and text with voiceover and videos.
# 
# While this time I will not explore these applications in detail, as they deserve more than just a shallow exploration, it is not difficult to imagine the potential for creating engaging storytelling applications that bring the travel journal – and other similar objects – to life for new audiences.
# 
# For example, using [Narakeet](https://www.narakeet.com/), a text-to-speech service that I chose due to offering Scottish accents amongst its voiceover options, we can create a narration that, along with AI-generated images can be used to engage younger audiences.
# 
# If we run the code below, we can listen to a fragment generated by Narakeet:

# In[1]:


import IPython.display as ipd
ipd.Audio('resources/audio/voiceover.mp3')


# Video generation applications that bring together narration, images video and other media can be also be used by cultural heritage institutions to engage audiences with their objects.
# 
# For example, when providing [VEED.io](https://www.veed.io) the following excerpt from the journal:
# 
# >On Friday (1 Nov.) Margaret unwell & confined to bed by cold. Being All Saints Day Mrs M. and I went at eleven to the Church of St Rock & heard remarkably fine chanting and singing. After lunch we took a voiture and drove to Notre Dame – the restoration, or cleaning & re-carving rather, of which, is now complete. Here also we heard fine music and saw the Archbishop of Paris in robes blazing with gold and his mitre on his head sitting with his clergy within the altar. Home by the boulevard des Italiens – table d’hote at six and spent the rest of the evening in the drawing room.
# 
# It generates the following video. Run the following code to watch it:

# In[29]:


from IPython.display import Video

Video("resources/video/veed_video.mp4")


# The output is an interpretation of the journal, using the likeness of one of the narrators available in the service. The narration does not look AI-generated, and could pass as a professional narration to the untrained eye.

# Inputting the same journal entry in [Invideo AI,](https://invideo.io/) with the additional prompt "1867 Travel journal entry depicting the travels of a Scottish gentleman and his family to Nice, France. This entry depicts a day in Paris", we get the following video.
# 
# Run the code to watch it:

# In[32]:


from IPython.display import Video

Video("resources/video/invideo_ai_video.mp4")


# Like VEED.io, Invideo AI interprets the journal entry and writes a script, but unlike VEED.io, it does not use the any human likeness. It also uses many more stock photos and videos, although they are not always relevant to the context of the journal entry.
# 
# While these technologies are currentlt limited to narrating scenes, Open AI is currently working on [Sora](https://openai.com/sora), a text-to-video model that promises to create realistic scenes from a prompt, similarly to how DALL-E 3 generates images.

# ## Conclusion
# 
# Using a custom GPT implementation running on ChatGPT-4, we set out to leverage generative AI's storytelling capabilities to offer new ways of enabling human creativity to interact with an obscure 19th-century manuscript travel journal. Creating a custom GPT application was extremely easy, but we cannot say it is accessible, as it requires a $20 monthly Chat-GPT Plus subscription – pricey for end-users, students and researchers. However, by making the custom GPT application public in the ChatGPT GPT Store and the dataset publicly available in Kaggle, we hope that a wider audience discovers this travel journal.
# 
# The custom GPT application generates new journal entries and sketches for places not described and situations not depicted in the original journal, following our prompts. While the GPT-4 model did not always mimic the writing or sketching style hof the author successfully, GPT-4 and DALL-E clearly offer audiences new and creative ways to interact with the journal data and metadata, expanding the author's storytelling and facilitating a connection between the author's creativity and that of the audience – even with more than 150 years of separation.
# 
# The analytic capabilities of the GPT-4 model and the journal data provided allow audiences to use prompts to ask about similarities and differences between how travel was conducted in the 19th century and how it is conducted today, inviting reflection and differents perspectives when engaging with the object. 
# 
# It is important to consider that this project has been fine-tuned using one single historical object. More accurate applications can be created by feeding the GPT-4 model more text or graphics created by the same author (difficult task, as we do not know the identity of the creator), or data and metadata extracted from other contemporary travel journals.
# 
# It is not difficult to imagine the applications for enhancing the ways we interact with the travel journal that generative AI enable. From enriched narrations that add historical and social context – for example, integrating sketches drawn by the author and AI-generated images, to combining different technologies that bring the author to life: using the likeness of an actor and voice-to-speech technologies to have the author "narrate" his entries, integrating historically accurate depictions of the places the author described, and even offering a "choose your own adventure" mode where the audience can continue writing the journal where its author left it off. When Sora becomes available, we could even imagine creating a "movie" that shows the author's travels using animated sketches.

# ## Further discussion
# - ['British travellers in early nineteenth-century registers and guest books'](https://www.tandfonline.com/doi/full/10.1080/13645145.2022.2084009) by Michael Heafford suggests a method for researching registers, guest books and other records that may help us identify the author of the journal referenced.
# - OpenAI is proposing Sora, a text-to-video diffusion model that promises to create realistic videos from text prompts. You can read the technical report [here](https://openai.com/research/video-generation-models-as-world-simulators).
# - The [_Dream Tapestry_ AI experience](https://thedali.org/press-room/dalle-at-the-dali-the-museums-collective-dream-experience/) at the [Salvador Dalí Museum](https://thedali.org/) in St. Petersburg, Florida invited visitors to share their personal dreams, which were then made into digital paintings, using the DALL-E 2 model (named after the Catalan artist). The results, some of which can be seen in [this video](https://www.youtube.com/watch?v=B0P4HHX7W7g), not only allowed visitors to visualise their dreams in a surrealist artistic fashion, but also brought together dreams of six different visitors in a single artwork, fostering human connections with the help of artificial intelligence.

# ## Bibliography

# 1. **Anonymous and Bob McLean**, ‘MS Gen 13: 19th Century Travel Journal with Illustrations, Transcript from Bob McLean’, 2016, Archives and Special Collections, University of Glasgow Library
# 2. **Buzard, James**, _The Beaten Track_ (Oxford University Press, 1993), 18–79 <https://doi.org/10.1093/acprof:oso/9780198122760.001.0001>
# 3. **Heafford, Michael**, ‘British Travellers in Early Nineteenth-Century Registers and Guest Books’, _Studies in Travel Writing, 25.3_ (2021), 374–88 <https://doi.org/10.1080/13645145.2022.2084009>
# 4. **Heath, Alex**, ‘All the News from OpenAI’s First Developer Conference’, _The Verge_, 2023 <https://www.theverge.com/2023/11/6/23948619/openai-chatgpt-devday-developer-conference-news> [accessed 14 April 2024]
# 5. **Hugging Face**, ‘Generation with LLMs’, _Hugging Face_ <https://huggingface.co/docs/transformers/en/llm_tutorial> [accessed 9 April 2024]
# 6. **Hugging Face**, ‘Fine-Tune a Pretrained Model’ <https://huggingface.co/docs/transformers/en/training> [accessed 9 April 2024]
# 7. **Lock, Samantha**, ‘What Is AI Chatbot Phenomenon ChatGPT and Could It Replace Humans?’, _The Guardian_, 5 December 2022, section Technology <https://www.theguardian.com/technology/2022/dec/05/what-is-ai-chatbot-phenomenon-chatgpt-and-could-it-replace-humans> [accessed 14 April 2024]
# 8. **OpenAI**, ‘Video Generation Models as World Simulators’, _OpenAI_, 2024 <https://openai.com/research/video-generation-models-as-world-simulators> [accessed 17 April 2024]
# 9. **Périz Rodríguez, Carmen**, ‘Travelling for Pleasure: A Brief History of Tourism’, _Europeana_, 2020 <https://www.europeana.eu/en/blog/travelling-for-pleasure-a-brief-history-of-tourism> [accessed 14 April 2024]
# 10. **PeterPan**, ‘Answer to “How Can I Play a Local Video in My IPython Notebook?”’, _Stack Overflow_, 2023 <https://stackoverflow.com/a/75844555> [accessed 17 April 2024]
# 11. **Roman, Iran R.**, ‘Jupyter Audio Basics’, _Musicinformationretrieval.com_ <https://musicinformationretrieval.com/ipython_audio.html> [accessed 17 April 2024]
# 12. **The Dalí Museum**, ‘DALL·E at The Dalí: The Museum’s Collective Dream Experience Is a Revolutionary Use of AI’, _Salvador Dalí Museum_ <https://thedali.org/press-room/dalle-at-the-dali-the-museums-collective-dream-experience/> [accessed 17 April 2024]
# 13. _The Dalí’s Dream Tapestry - A Collective Dream Experience_, dir. by **The Dalí Museum**, 2022 <https://www.youtube.com/watch?v=B0P4HHX7W7g> [accessed 17 April 2024]
# 14. **Thompson, Carl**, ‘Nineteenth-Century Travel Writing’, in _The Cambridge History of Travel Writing_, ed. by Nandini Das and Tim Youngs, 1st edn (Cambridge University Press, 2019), pp. 108–24 <https://doi.org/10.1017/9781316556740.008>
# 15. **Vaswani, Ashish, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, and others**, ‘Attention Is All You Need’ (arXiv, 2017) <http://arxiv.org/abs/1706.03762> [accessed 14 April 2024]
# 16. **Zelazko, Alicja**, ‘Grand Tour | European, Itinerary, Countries, & Tourism | Britannica’, _Encycloaedia Britannica_, 2024 <https://www.britannica.com/topic/grand-tour> [accessed 14 April 2024]
# 
