package equipo._7.SentimentAPI.controller;

import equipo._7.SentimentAPI.domain.user.*;
import equipo._7.SentimentAPI.infra.security.DataTokenJWT;
import equipo._7.SentimentAPI.infra.security.TokenService;
import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Objects;

@RestController
@RequestMapping
public class AuthController {

    @Autowired
    private TokenService tokenService;
    @Autowired
    private AuthenticationManager manager;
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private PasswordEncoder passwordEncoder;

    @PostMapping("/login")
    public DataTokenJWT login(@RequestBody @Valid DataAuth data) {
        var authToken = new UsernamePasswordAuthenticationToken(data.email(), data.password());
        var auth = manager.authenticate(authToken);
        var tokenJwt = tokenService.generateToken((User) auth.getPrincipal());
        return new DataTokenJWT(tokenJwt);
    }

    @Transactional
    @PostMapping("/register")
    public DataTokenJWT register(@RequestBody @Valid DataRegister data) {
        if (!Objects.equals(data.password(), data.passwordConfirmation())) {
            throw new RuntimeException("Passwords do not match");
        }
        var user = new User(data.email(), encodePassword(data.password()));
        userRepository.save(user);
        var authToken = new UsernamePasswordAuthenticationToken(data.email(), data.password());
        var auth = manager.authenticate(authToken);
        var tokenJwt = tokenService.generateToken((User) auth.getPrincipal());
        return new DataTokenJWT(tokenJwt);
    }

    @GetMapping("/users")
    public List<DataUsers> users (@PageableDefault(size = 10) Pageable pageable) {
        Page<DataUsers> page = userRepository.findAll().stream().map();
    }

    private String encodePassword(String password) {
        return passwordEncoder.encode(password);
    }
}
