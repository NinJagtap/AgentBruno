#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 06:22:52 2024

@author: ninadjagtap
"""
from AgentBruno.storm import Storm
import asyncio
import streamlit as st

async def main():    
    
    """
    Mandatory parameters: 
    You will need to pass in the topic and OpenAI API key
    """
    topic = 'Navigating Risk - Considerations for Migrating SCADA Solutions to the Cloud'
    open_ai_key = st.secrets["OPENAI_API_KEY"]
    
    """
    #Optional Parameters: 
    If you have a private domain/company specific PineCone VectorStore, you can attach it for finer details. 
    Passing the pinecone vectorstore is optional. If you dont have the vector store - the code will still work and will perform research over internet.
    """
    pinecone_api_key = ""
    pinecone_envo = ""
    pinecone_index = ""
    
    # However, by passing the domain or company specific vectorstore, the code will use it for researching the topic in addition to researching for topic on internet. 
    # pinecone_api_key = st.secrets['PINECONE_API_KEY']
    # pinecone_envo = st.secrets['PINECONE_ENV']
    # pinecone_index = st.secrets['PINECONE_INDEX']
    
    # Create an instance of the Storm class
    storm_instance = Storm(topic, open_ai_key, pinecone_api_key, pinecone_envo, pinecone_index)

    # Call the write_storm_article method on the storm_instance
    
    article = await storm_instance.write_storm_article()
    
    st.write(article)
    
if __name__ == '__main__':
    asyncio.run(main())

