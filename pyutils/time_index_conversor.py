
def get_interval_params( interval ) :

	interval_value = int( interval[ :-1 ] ) ;
	interval_type = interval[ -1 ] ;

	return interval_value , interval_type ;

################################################################################
#################################### D A Y S ###################################
################################################################################

def days_to_idx( days , interval ) :

	interval_value , interval_type = get_interval_params( interval ) ;
	
	if ( interval_type == 'd' ) : return int( days / interval_value ) ;
	
	elif( interval_type == 'h' ) : return int( days * 24.0 / interval_value ) ;
	
	else : return int( days * 24.0 * 60.0 / interval_value ) ;


def idx_to_days( idx , interval ) :
	
	interval_value , interval_type = get_interval_params( interval ) ;
	
	if ( interval_type == 'd' ) : return ( idx * interval_value ) ;
	
	elif ( interval_type == 'h' ) : return ( idx * interval_value ) / 24.0 ;
	
	else : return ( idx * interval_value ) / ( 24.0 * 60.0 ) ;

################################################################################
################################### H O U R S ##################################
################################################################################

def hours_to_idx( hours , interval ) :

	interval_value , interval_type = get_interval_params( interval ) ;

	if ( interval_type == 'd' ) : return int ( hours / interval_value / 24.0 ) ;

	elif ( interval_type == 'h' ) : return int( hours ) ;

	elif ( interval_type == 'm' ) : return int( hours * 60 / interval_value ) ;


def idx_to_hours( idx , interval ) :

	interval_value , interval_type = get_interval_params( interval ) ;

	if ( interval_type == 'd' ) : return ( idx * interval_value * 24.0 ) ;

	elif ( interval_type == 'h' ) : return idx ;

	elif ( interval_type == 'm' ) : return idx * interval_value / 60.0 ;