def classify(features_train, labels_train):

    from sklearn import tree
    clf2 = tree.DecisionTreeClassifier(min_samples_split=2)
    clf50 = tree.DecisionTreeClassifier(min_samples_split=50)

    clf2.fit(features_train, labels_train)
    clf50.fit(features_train, labels_train)

    acc_min_samples_split_2 = clf2.score(features_test, labels_test)
    acc_min_samples_split_50 = clf50.score(features_test, labels_test)

    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier.fit(features_train, labels_train)
    return classifier
