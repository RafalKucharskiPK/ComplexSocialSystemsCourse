1. Create a real-time open trip planner (OTP) for a chosen city using GTFS-RT(real-time data).
2. Analyze urban accessibility by identifying and mapping wheelchar-friendly routes using OSM data. Detect sidewalks, crossings, curbs, inclines, and accessibility features and compute optimal routes for people with mobility impairments. Create a web-based app for route planning.
3. Select a specific region and download its OpenStreetMap (OSM) network. Convert the extracted data into a suitable format for use in SUMO (Simulation of Urban Mobility). Then, train autonomous vehicle (AVs) agents to find the fastest route using Multi-Agent Reinforcement Learning (MARL) algorithm implemented with the TorchRL library. 
4. For $n$ students, each with individual ranking of topics $n \to s$, assign them to $i$ topics. Each topic needs to be occupied, some with two persons. Which is a variation of a classic college admission problem (generalization of marriage problem). But here you maximise your 'satisfaction' - how happy and fair is the group with the assignment. Can you cheat to get your desired topic?
5. Urban growth and gentrification modeling. Simulate urban growth and gentrification using agent-based model. The model should capture how residents, developers, and policies interact over time, influencing housing prices, migration, and neighborhood evolution. The city can be modeled aa a grid based system, where each cell represents a neighborhood or housing unit and has an initial property value. The agents of the system are the residents, that have an income level, the developers and identify low-cost properties to purchase and upgrade and government policies, like tax incentives, zoning laws or rent control. Questions that can be answered:
    * How does gentrification emerge in an agent-based city model?
    * What factors accelerate or slow down gentrification?
    * How do different government policies impact urban growth?
6. Analyze the impact of subsidization strategies on user adoption, retention, and profitability in two-sided platforms. By leveraging real-world data and econometric models, determine whether subsidies effectively drive long-term platform growth or only cause temporary adoption spikes.
    * Extract real-world platform data from kaggle, public company reports, google trends or web scrapping.
    * Process and analyze this data.
    * Visualize and interpret them.
7. Replicating human decision-making using inverse reinforcement learning
    * Replicate human decision-making behavior (from the Swissmetro dataset and/or any other of the student’s choice) using inverse reinforcement learning and compare the performance of the learned policies with discrete choice models (such as multinomial logit models).
    * Many resources/similar works available. Some of my choices: 
        * https://www.sciencedirect.com/science/article/pii/S0968090X23000682?casa_token=f3tSWLqW9nIAAAAA:MMX3g_rEaGi93JVVOTIEsCx0IZAwv_Ue3S-PFgvH1iq9qHvCq4IZciJbECjuS4Qj6kXCde2p
        * https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6969b30ccd2f38c0b67e335e75f9483343a1c301
8. Academic co-authorship network properties over the years
    * Analyzing the emergence of small-world property in co-authorship networks for a specific scientific discipline over the years. How has the structure of co-authorship networks in the chosen field evolved over the last (say) 25 years, and does it exhibit small-world characteristics? Is it be affected by emerging interdisciplinary collaborations?
    *  Students may use free APIs and/or open-source datasets such as arxiv, Microsoft Academic Graph, etc.
    *  https://en.wikipedia.org/wiki/Small-world_network
    *  Can be helpful:
        * https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0121129
        * https://iopscience.iop.org/article/10.1088/1742-6596/2099/1/012055/meta
9. How does network connectivity affect the speed of information diffusion in a real-world Twitter dataset?
    * Simulating a fake new propagation in a social media network (such as X) using virus-spreading models. By adding random connections for emulating bots and “For You” page, analyzing the changes in fake news dissemination.
    *  Can be useful:
        * https://osome.iu.edu/resources/publication-data
10. Balancing cooperation vs individual incentives in a mixed-motive multi-agent game
    * Modeling and simulating a multi-agent game where each agent receives directions from a central controller. System optimality is achieved with full compliance, but agents may benefit from defecting to the controller’s directions. However, if too many defects, the system collapses, like in real-world social dilemmas such as traffic congestion or public goods depletion. The problem can be framed as a Price of Anarchy problem, with some global efficiency loss by self-interested agents.
    *  This can be modeled with some (possibly adjusted) PettingZoo environment or some arbitrary game to be implemented by the student.
    *  Agents and controllers can be RL agents, or a rule-based system and discrete choice agents. If the second option is chosen, it’d be interesting to see in which parts of parameterization spaces we see the system collapse.
    *  Can be helpful:
        * https://arxiv.org/abs/2010.00575
        * https://arc.aiaa.org/doi/abs/10.2514/6.2025-1929
11. Optimal bus fare management
    * In a small town network, modeling human drivers (using discrete choice models, which can be from Biogeme) and simulating their mode selection for a daily commute scenario. Defining arbitrary costs like discomfort, travel time, and fares for agents to minimize over time. Using an (optionally) agent-based simulator like SUMO, adding bus lines that drivers may prefer over their private cars. Finding (either brute force or optimization algorithms) optimal/feasible bus fares for mitigating congestion in a city. Analyzing how this changes depending on the scale, population size, bus frequency, and human parameterization. Making insightful visualizations showcasing correlations.
    * Optional, can be a starting point: https://github.com/naronald/SUMOoD
    * Some related works:
        * https://link.springer.com/article/10.1007/s10489-024-05869-1
        * https://link.springer.com/article/10.1007/s11116-019-10074-y
    *  Using a similar framework, it might also be interesting to analyze optimal ticket control frequencies (designer) vs ticket purchase decisions (commuters).
12. Do social media recommendation systems represent their creators’ bias?
    * Analyzing social media recommendation datasets to look for recommendation patterns before critical events in near history (elections, vaccinations, etc.). Can we find bias/imbalance towards a certain ideology?
    * Data is quite sparse for this. A good candidate for analysis could be: https://foundation.mozilla.org/en/youtube/regretsreporter-dataset/
    * Can be helpful:
        * https://www.researchgate.net/publication/378233520_Analyzing_Bias_in_Recommender_Systems_A_Comprehensive_Evaluation_of_YouTube%27s_Recommendation_Algorithm
        * https://www.sciencedirect.com/science/article/pii/S2468696419300886

# Last Year’s Projects

* Finding causes of conflicts in Reddit network
  * SNAP database provides embeddings of many subreddits as well as the network of subreddit hyperlinks with ready-to-use characterisation of the hyperlink context. We will try to find which characteristics are can lead to conflicts.
  * https://snap.stanford.edu/data/soc-RedditHyperlinks.html

* Comparison of Social Force Models
  * There are papers that try to extend the original SFM by adding additional forces. I want to implement the extended model and compare it with the original.
  * https://snap.stanford.edu/data/soc-RedditHyperlinks.html

* Preferences for car-free city center (discrete choice models)
  * We want to implement models and establish what kinds of people prefer car-free city center (in Berlin) vs who are against
  * https://www.sciencedirect.com/science/article/abs/pii/S1361920915300626?via%3Dihub

* High-End Lifestyle Profiling
  * Development of behavioral profiles of wealthy individuals and segmentation into homogeneous groups with similar characteristics and preferences.
  * https://www.kaggle.com/datasets/anthonytherrien/luxury-lives-a-data-driven-glimpse/data

* Percolations in human movement
  * Monte carlo simulations of percolations in crowds (or human movement in general) with a possible extension to graph-based optimisation methods
  * https://www.kaggle.com/datasets/anthonytherrien/luxury-lives-a-data-driven-glimpse/data

* Optimal traffic light configuration
  * Explore different approaches to traffic light state changing
  * See Sumo-RL

* Reinforcement Learning in Sequential Social Dilemma
  * Explore the effect of different parameters of the environment in social dillema game
  * https://github.com/eugenevinitsky/sequential_social_dilemma_games/tree/master

