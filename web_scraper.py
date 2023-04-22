from bs4 import BeautifulSoup
TEST_HTML = open("test_string.txt", "r").read()

def get_tag_data(html, tag):
    """
    Returns a dictionary out of the HTML data from all <`tag`> tags in `html`.
    
    Parameters:
    	`html` {str}: HTML data to be scrapped
    
    	`tag` {str}: HTML tag. Must be a valid tag
    
    Returns:
    	dict {str -> bs4.element.tag}: Dictionary containing all tags with tag's property 
    							as key and the element as value
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # list of tags placeholder attr
    question_tags = soup.find_all(tag)
    
    # create tuple of property name and inputs
    property_input_tup = map(lambda qt: (qt.get('property'), qt.find('input')), question_tags)
    
    # filter tags that have no input or no property name
    filtered_property_input =  filter(lambda item: item[0] != None and item[1] != None, property_input_tup)
    
    # make a dictionary
    question_names = dict(list(filtered_property_input))

    return question_names

def trim_html(data, threshold):
    """
    
    """
    
    s = ''
    final_elements = []
    for element in data:
        
        element_string = str(element)
        
        if len(s) + len(element_string) > threshold:
            
            # append whatever there is
            final_elements.append(s)
            
            # reset
            s = element_string
            
        else:
            # add line break + element as HTML tag
            s += '\n' + element_string
            
    final_elements.append(s)
            
    return final_elements
        
        

if __name__ == '__main__':
    data_dict = get_tag_data(TEST_HTML, 'question')
    
    print('length of HTML data', len(TEST_HTML))
    
    print('data dict keys are: ', data_dict.keys())
    
    trimmed_list = trim_html(data_dict.values(), 120_000)
    
    print('len trimmed list: ', len(trimmed_list))
    
    print('trimmed list: ', trimmed_list)
    
    print('chunks size:', len(trimmed_list[0]))   
    